var app=getApp();

function update_globalData_msgList_default(msg){//其他页面收到新消息后更新全局变量消息列表
  for (var i = 0; i < msg.length; i++) { 
    msg[i]['isread']=0;
    if(msg[i]['from']==app.globalData.user){//添加到消息列表
      if(!(msg[i]['to'] in app.globalData.msgList)){//若未存在与此人的聊天记录数组，就新建一个后再push
        app.globalData.msgList[msg[i]['to']]=[]
      }
      app.globalData.msgList[msg[i]['to']].push(msg[i]);
    }else{
      if(!(msg[i]['from'] in app.globalData.msgList)){
        app.globalData.msgList[msg[i]['from']]=[]
      }
      app.globalData.msgList[msg[i]['from']].push(msg[i]);
    } 
  }

}

function update_globalData_msgList_chatting(msg,to_name){//chatting页面收到新消息后更新全局变量消息列表
  for (var i = 0; i < msg.length; i++) { 
    if(msg[i]['from']!=to_name){//如果不是当前正在聊天的，就将已读改为未读
      msg[i]['isread']=0;
    }
    if(msg[i]['from']==app.globalData.user){//添加到消息列表
      if(!(msg[i]['to'] in app.globalData.msgList)){//若未存在与此人的聊天记录数组，就新建一个后再push
        app.globalData.msgList[msg[i]['to']]=[]
      }
      app.globalData.msgList[msg[i]['to']].push(msg[i]);
    }else{
      if(!(msg[i]['from'] in app.globalData.msgList)){
        app.globalData.msgList[msg[i]['from']]=[]
      }
      app.globalData.msgList[msg[i]['from']].push(msg[i]);
    } 
  }

}

function update_chatting_history(to_name){//将与当前人的聊天记录均改为已读
  for(let i in app.globalData.msgList[to_name]){
    app.globalData.msgList[to_name][i]["isread"]=1;
  }
}

module.exports={//导出上面这些函数，方式为 引用名：函数名，在别的界面导入后就可以用引用名调用这个函数了
  update_globalData_msgList_default:update_globalData_msgList_default, 
  update_globalData_msgList_chatting:update_globalData_msgList_chatting,
  update_chatting_history:update_chatting_history
}
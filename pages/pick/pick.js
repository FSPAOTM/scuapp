Page({
  data: {
    buttons: [
      { id: 1, name: '家教' }, 
      { id: 2, name: '服务员' }, 
      { id: 3, name: '实习' },
      { id: 4, name: '客服' }, 
      { id: 5, name: '调研' },
      { id: 6, name: '摄影剪辑' },
      { id: 7, name: '文案编辑' },
      { id: 11, name: '会展活动' },
      { id: 13, name: '销售导购' },
      { id: 14, name: '演出' },
      { id: 15, name: '翻译' },
      { id: 16, name: '模特礼仪' },
      { id: 17, name: '设计' },
      { id: 18, name: '其他' }
  ],

   
  },

  onLoad: function (options) {
    this.data.buttons[0].checked = true;
    this.setData({
      buttons: this.data.buttons,
    })
  },

/**
 * 事件监听,实现单选效果
 * e是获取e.currentTarget.dataset.id所以是必备的，跟前端的data-id获取的方式差不多
 */
radioButtonTap: function (e) {
  console.log(e)
  let id = e.currentTarget.dataset.id
  console.log(id)
  for (let i = 0; i < this.data.buttons.length; i++) {
    if (this.data.buttons[i].id == id) {
      //当前点击的位置为true即选中
      this.data.buttons[i].checked = true;
    }
    else {
      //其他的位置为false
      this.data.buttons[i].checked = false;
    }
  }


  this.setData({
    buttons: this.data.buttons,
  })
},

})
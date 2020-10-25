// pages/modification/modification.js
var app = getApp()
Page({
 
  data: {
    myinfo:null,
    hiddenmodalput: true,
  },
  
//点击按钮痰喘指定的hiddenmodalput弹出框

modalinput: function () {
 
this.setData({
 
hiddenmodalput:!this.data.hiddenmodalput,
})
 
},
 
//取消按钮
 
cancel: function () {
 
this.setData({
 
hiddenmodalput: true,
});
 
},
 
//确认
 
confirm: function () {
 
this.setData({
 
hiddenmodalput: true,

})
 
}
 
})

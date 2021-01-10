// pages/infoShow/infoShow.js个人简历展示页面并提供完善入口
const app = getApp();
Page({
  data: {
    edu: "",
    name: "",
    age: "",
    gender: "",
    tech: "",
    job: "",
    project: "",
    practice: "",
    works: "",
  },

  change: function () {
    wx.redirectTo({
      url: '../sinfoFill/sinfoFill',
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (e) {
    wx.request({
      url: app.globalData.url + '/Insert_resume_show/',
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      method: "POST",
      data: {
        stuNumber: app.globalData.user,
      },
      success: (res) => {
        console.log(res);
        console.log(this.data.stuNumber);
        if (res.statusCode == 200) {
          console.log(res.data);
          this.setData({
            name: res.data.name,
            age: res.data.age,
            gender: res.data.sex,
            tech: res.data.res_asses,
            edu: res.data.res_edu,
            job: res.data.res_work,
            project: res.data.res_proj,
            practice: res.data.res_extra,
            works: res.data.res_per,
          })
          app.globalData.age = this.data.age;
          console.log(app.globalData.age);
        }
      }
    })
  }
})
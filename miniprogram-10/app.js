//app.js
var app=getApp()
App({
  onLaunch: function () {
    // 展示本地存储能力
    var logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)
    // 登录
    wx.login({
      success: res => {
        // 发送 res.code 到后台换取 openId, sessionKey, unionId
        if (res.code) {
          wx.request({
            url: app.globalData.url + '//', //待修改
            header: {
              'content-type': 'application/json'
            },
            data: {
              code: res.code
            },
            method: 'GET',
            success: res => {
              if (res.statusCode == 200) {
                wx.request({
                  url: app.globalData.url + "Login/setuser",//待修改
                  method:"POST",
                  data: {
                    openid: res.data.openid
                  },
                  header: {
                    'content-type': 'application/x-www-form-urlencoded'
                  },
                  success(res) {
                    //如果有该用户，把用户信息放到公共数组中
                    if (res.data) {
                      app.globalData.userInfo = res.data
                    }
                  },
                })
              }
            }
          })
        }
      }
    })
    // 获取用户信息
    wx.getSetting({
      success: res => {
        if (res.authSetting['scope.userInfo']) {
          // 已经授权，可以直接调用 getUserInfo 获取头像昵称，不会弹框
          wx.getUserInfo({
            success: res => {
              // 可以将 res 发送给后台解码出 unionId
              this.globalData.userInfo = res.userInfo

              // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
              // 所以此处加入 callback 以防止这种情况
              if (this.userInfoReadyCallback) {
                this.userInfoReadyCallback(res)
              }
            }
          })
        }
      }
    })
  },

  //第一种底部  
  editTabBar: function () {
    //使用getCurrentPages可以获取当前加载中所有的页面对象的一个数组，数组最后一个就是当前页面。

    var curPageArr = getCurrentPages(); //获取加载的页面
    var curPage = curPageArr[curPageArr.length - 1]; //获取当前页面的对象
    var pagePath = "../miniprogram-10/pages/login/login"; //当前页面url
    if (pagePath.indexOf('/') != 0) {
      pagePath = '/' + pagePath;
    }

    var tabBar = this.globalData.tabBar;
    for (var i = 0; i < tabBar.list.length; i++) {
      tabBar.list[i].active = false;
      if (tabBar.list[i].pagePath == pagePath) {
        tabBar.list[i].active = true; //根据页面地址设置当前页面状态    
      }
    }
    curPage.setData({
      tabBar: tabBar
    });
  },
  //第二种底部，原理同上
  editTabBar1: function () {
    var curPageArr = getCurrentPages();
    var curPage = curPageArr[curPageArr.length - 1];
    var pagePath = "../miniprogram-10/pages/login/login";
    if (pagePath.indexOf('/') != 0) {
      pagePath = '/' + pagePath;
    }
    var tabBar = this.globalData.tabBar1;
    for (var i = 0; i < tabBar.list.length; i++) {
      tabBar.list[i].active = false;
      if (tabBar.list[i].pagePath == pagePath) {
        tabBar.list[i].active = true;
      }
    }
    curPage.setData({
      tabBar: tabBar
    });
  },


  globalData: {
    list: [],
    url: 'http://127.0.0.1:8000/wechat',
    userInfo: "",
    user: "",
    age: "",
    gender: "",
    edu: "",
    tech: "",
    job: "",
    project: "",
    practice: "",
    works: "",
    stuNumber: "",
    jobType: "",
    ow_number: "",
    tabBar: {
      "color": "#a9b7b7",
      "selectedColor": "#11cd6e",
      "borderStyle": "white",
      "list": [{
          "selectedIconPath": "2.png",
          "iconPath": "1.png",
          "pagePath": "pages/sallJob/sallJob",
          "text": " 全部兼职",
          "class": "menu-item",
          "active": false
        },
        {
          "selectedIconPath": "4.png",
          "iconPath": "3.png",
          "pagePath": "pages/smyJob/smyJob",
          "text": "我的兼职",
          "class": "menu-item",
          "active": false
        },
        {
          "selectedIconPath": "6.png",
          "iconPath": "5.png",
          "pagePath": "pages/scenter/scenter",
          "text": "个人中心",
          "class": "menu-item",
          "active": false
        }
      ],
      "position": "bottom"
    },
    "tabBar1": {
      "color": "#a9b7b7",
      "selectedColor": "#11cd6e",
      "borderStyle": "white",
      "list": [{
          "selectedIconPath": "1.png",
          "iconPath": "2.png",
          "pagePath": "pages/workspace/workspace",
          "text": " 工作区",
          "class": "menu-item1",
          "active": false
        },
        {
          "selectedIconPath": "3.png",
          "iconPath": "4.png",
          "pagePath": "pages/fabu/fabu",
          "text": "我的发布",
          "class": "menu-item1",
          "active": false
        },
        {
          "selectedIconPath": "5.png",
          "iconPath": "6.png",
          "pagePath": "pages/mancenter/mancenter",
          "text": "企业中心",
          "class": "menu-item1",
          "active": false
        }
      ],
      "position": "bottom"
    }
  }
})
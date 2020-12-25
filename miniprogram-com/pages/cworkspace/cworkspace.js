// pages/cworkspace/cworkspace.js
const app = getApp();
var dateTimePicker = require('outer3.js');
Page({

  /**
   * 页面的初始数据
   */
  data: {
    showIndex: "",
    show: false,
    //tap切换自定义宽高
    winWidth: 0,
    winHeight: 0,
    // tab切换，方法一

    scrollleft: 0,
    currentTab: 0,

    idArr: [

    ],
    hiddenmodalput: true,
    dateTimeArray: null,
    dateTime: null,
    dateTimeArray1: null,
    dateTime1: null,
    startYear: 2020,
    endYear: 2022,
    workinfo1: [],
    workinfo2: [],
    workinfo3: [],
    workinfo4: [],
    workinfo5: [],
    mingdan: [],
    numbers: [],
    count: "",
    baodaotime1: "",
    beizhu: ""
  },

  modalput() {
    this.setData({
      hiddenmodalput: !this.data.hiddenmodalput,
    })
  },

  swichNav: function (e) {
    var that = this;
    if (this.data.currentTab === e.target.dataset.current) {
      return false;
    } else {
      that.setData({
        currentTab: e.target.dataset.current
      })
    }
  },

  checkCor: function () {
    if (this.data.currentTab > 4) {
      this.setData({
        scrollleft: 300
      })
    } else {
      this.setData({
        scrollleft: 0
      })
    }
  },

  listDataClick(e) {
    if (e.currentTarget.dataset.index != this.data.showIndex) {
      this.setData({
        showIndex: e.currentTarget.dataset.index
      })
    } else {
      this.setData({
        showIndex: 0
      })
    }
  },


  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;
    if (options.currentTab != '') {
      that.setData({
        currentTab: options.currentTab
      })
    }
    /** 
     * 获取系统信息,系统宽高
     */
    wx.getSystemInfo({
      success: function (res) {
        that.setData({
          winWidth: res.windowWidth,
          winHeight: res.windowHeight
        });
      }
    });

    wx.request({
      url: app.globalData.url + '/Show_applicant/',
      header: {
        'Content-Type': 'application/json'
      },
      method: "GET",
      data: {
        user: app.globalData.user
      },
      success: function (res) {
        console.log(res);
        var i;
        var baominger = []
        for (i = 0; i < res.data.length; i++) {
          if (res.statusCode == 200) {
            if (res.data[i].status == "待审核") {
              var baoming = {}
              var person = {}
              var count = 0
              if (that.data.workinfo1.length >= 1) {
                var m;
                for (m = 0; m < that.data.workinfo1.length; m++) {
                  if (res.data[i].ow_number == that.data.workinfo1[m].baominger[0].ow_number) {
                    baoming.ow_number = res.data[i].ow_number;
                    baoming.user = res.data[i].user;
                    baoming.stu_number = res.data[i].stu_number;
                    that.data.workinfo1[m].baominger.push(baoming)
                    that.setData({
                      workinfo1: that.data.workinfo1
                    })
                    break;
                  } else {
                    count = count + 1
                  }
                }
                if (count == that.data.workinfo1.length) {
                  var baominger2 = []
                  baoming.ow_number = res.data[i].ow_number;
                  baoming.user = res.data[i].user;
                  baoming.stu_number = res.data[i].stu_number;
                  baominger2.push(baoming)
                  person.post = res.data[i].post
                  person.baominger = baominger2
                  that.data.workinfo1.push(person)
                  that.setData({
                    workinfo1: that.data.workinfo1
                  })
                }
              } else {
                baoming.ow_number = res.data[i].ow_number;
                baoming.user = res.data[i].user;
                baoming.stu_number = res.data[i].stu_number;
                baominger.push(baoming)
                baominger = baominger
                person.post = res.data[i].post
                person.baominger = baominger
                that.data.workinfo1.push(person)
                that.setData({
                  workinfo1: that.data.workinfo1
                })
              }
              console.log(that.data.workinfo1)
            } else if (res.data[i].status == "表筛未通过") {
              that.data.workinfo2.push(res.data[i])
              that.setData({
                workinfo2: that.data.workinfo2
              })
            } else if (res.data[i].status == "未录用") {
              that.data.workinfo2.push(res.data[i])
              that.setData({
                workinfo2: that.data.workinfo2
              })
            } else if (res.data[i].status == "表筛通过") {
              that.data.workinfo3.push(res.data[i])
              that.setData({
                workinfo3: that.data.workinfo3
              })
            } else if (res.data[i].status == "面试中") {
              that.data.workinfo3.push(res.data[i])
              that.setData({
                workinfo3: that.data.workinfo3
              })
            } else if (res.data[i].status == "已录用") {
              that.data.workinfo4.push(res.data[i])
              that.setData({
                workinfo4: that.data.workinfo4
              })
            } else if (res.data[i].status == "工作结束") {
              that.data.workinfo5.push(res.data[i])
              that.setData({
                workinfo5: that.data.workinfo5
              })
            } else if (res.data[i].status == "待评价") {
              that.data.workinfo5.push(res.data[i])
              that.setData({
                workinfo5: that.data.workinfo5
              })
            } else if (res.data[i].status == "已评价") {
              that.data.workinfo5.push(res.data[i])
              that.setData({
                workinfo5: that.data.workinfo5
              })
            }
          }
        }
      }
    });
    // 获取完整的年月日 时分秒，以及默认显示的数组
    var obj = dateTimePicker.dateTimePicker(this.data.startYear, this.data.endYear);
    var obj1 = dateTimePicker.dateTimePicker(this.data.startYear, this.data.endYear);
    // 精确到分的处理，将数组的秒去掉
    var lastArray = obj1.dateTimeArray.pop();
    var lastTime = obj1.dateTime.pop();
    this.setData({
      dateTime: obj.dateTime,
      dateTimeArray: obj.dateTimeArray,
      dateTimeArray1: obj1.dateTimeArray,
      dateTime1: obj1.dateTime,
    })
  },

  changeDateTimeColumn1(e) {
    var arr = this.data.dateTime1,
      dateArr = this.data.dateTimeArray1;

    arr[e.detail.column] = e.detail.value;
    dateArr[2] = dateTimePicker.getMonthDay(dateArr[0][arr[0]], dateArr[1][arr[1]]);

    this.setData({
      dateTimeArray1: dateArr,
      dateTime1: arr,
      baodaotime1: (2020 + arr[0]) + "-" + (1 + arr[1]) + "-" + (1 + arr[2]) + " " + arr[3] + ":" + arr[4]
    });
  },

  blurbeizhu(e) {
    this.setData({
      beizhu: e.detail.value
    })
  },

  itemSelected: function (e) {
    var index = e.currentTarget.dataset.index;
    var item = this.data.workinfo3[index];
    item.isSelected = !item.isSelected;
    this.setData({
      workinfo3: this.data.workinfo3
    })

    //获取选中学生数
    var content = {}
    content.ow_number = item.ow_number;
    content.stu_number = item.stu_number;
    if (this.data.mingdan.length >= 1) {
      var i;
      if (item.isSelected) {
        for (i = 0; i < this.data.mingdan.length; i++) {
          if (item.ow_number != this.data.mingdan[i].ow_number || item.stu_number != this.data.mingdan[i].stu_number) {
            this.data.mingdan.push(content)
            this.setData({
              mingdan: this.data.mingdan
            })
            break;
          }
        }
      } else if (!item.isSelected) {
        var j;
        for (j = 0; j < this.data.mingdan.length; j++) {
          if (item.ow_number == this.data.mingdan[j].ow_number && item.stu_number == this.data.mingdan[j].stu_number) {
            this.data.mingdan.splice(j, 1)
            this.setData({
              mingdan: this.data.mingdan
            })
          }
        }
      }
    } else {
      this.data.mingdan.push(content)
      this.setData({
        mingdan: this.data.mingdan
      })
    }
    console.log(this.data.mingdan)

    //获取选中工作总数
    if (this.data.numbers.length >= 1) {
      var ii;
      if (item.isSelected) {
        for (ii = 0; ii < this.data.numbers.length; ii++) {
          if (item.ow_number != this.data.numbers[ii].ow_number) {
            this.data.numbers.push(this.data.mingdan[ii])
            this.setData({
              numbers: this.data.numbers
            })
            break;
          }
        }
      } else if (!item.isSelected) {
        var jj;
        for (jj = 0; jj < this.data.numbers.length; jj++) {
          if (this.data.mingdan.length >= 1) {
            if (item.ow_number != this.data.numbers[jj].ow_number) {
              this.data.numbers.splice(jj, 1)
              this.setData({
                numbers: this.data.numbers
              })
            }
          } else {
            if (item.ow_number == this.data.numbers[0].ow_number) {
              this.data.numbers.splice(0, 1)
              this.setData({
                numbers: this.data.numbers
              })
            }
          }
        }
      }
    } else {
      this.data.numbers.push(this.data.mingdan[0])
      this.setData({
        numbers: this.data.numbers
      })
    }
    var count = this.data.numbers.length
    this.setData({
      count: count
    })
  },

  /**
   * 弹窗
   */
  showDialogBtn: function () {
    this.setData({
      hiddenmodalput: !this.data.hiddenmodalput
    })
  },

  /**
   * 弹出框蒙层截断touchmove事件
   */
  preventTouchMove: function () {},


  /**
   * 对话框取消按钮点击事件
   */
  cancel: function () {
    this.setData({
      hiddenmodalput: true
    });
  },
  /**
   * 对话框确认按钮点击事件
   */
  confirm: function () {
    wx.request({
      url: app.globalData.url + '/Com_work_employed/', //已通过名单
      method: "POST",
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      data: {
        mingdan: JSON.stringify(this.data.mingdan),
        count: this.data.count,
        time: this.data.baodaotime1,
        beizhu: this.data.beizhu,
      },
      success: (res) => {
        if (res.statusCode == 200) {
          if (res.data == "未面试，尚不能发送结果") {
            wx.showToast({
              title: '未面试，尚不能发送结果',
              icon: 'none',
              duration: 2000
            })
            setTimeout(function () {
              this.onRefresh()
            }, 2000)
          } else if (res.data == "面试中，尚不能发送结果") {
            wx.showToast({
              title: '面试中，尚不能发送结果',
              icon: 'none',
              duration: 2000
            })
            setTimeout(function () {
              this.onRefresh()
            }, 2000)
          } else if (res.data == "通知成功") {
            this.setData({
              mingdan: [],
              count: "",
              time: "",
              beizhu: ""
            })
            this.setData({
              hiddenmodalput: true
            });
            wx.showToast({
              title: '通知成功',
              icon: 'success',
              duration: 2000
            })
            setTimeout(function () {
              this.onRefresh()
            }, 2000)
          }
        }
      }
    })
  },

  weitongguo() {
    wx.request({
      url: app.globalData.url + '/Com_work_unemployed/', //未通过名单
      method: "POST",
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      data: {
        mingdan: JSON.stringify(this.data.mingdan),
        count: this.data.count,
      },
      success: (res) => {
        if (res.statusCode == 200) {
          if (res.data == "未面试，尚不能发送结果") {
            wx.showToast({
              title: '未面试，尚不能发送结果',
              icon: 'none',
              duration: 2000
            })
            setTimeout(function () {
              this.onRefresh()
            }, 2000)
          } else if (res.data == "面试中，尚不能发送结果") {
            wx.showToast({
              title: '面试中，尚不能发送结果',
              icon: 'none',
              duration: 2000
            })
            setTimeout(function () {
              this.onRefresh()
            }, 2000)
          } else if (res.data == "通知成功") {
            this.setData({
              mingdan: [],
              count: "",
            })
            wx.showToast({
              title: '通知成功',
              icon: 'none',
              duration: 2000
            })
            setTimeout(function () {
              this.onRefresh()
            }, 2000)
          }
        }
      }
    })
  },


  yibaoming: function (ev) {
    var that = this;
    var ow_number = ev.currentTarget.dataset.name1;
    var stu_number = ev.currentTarget.dataset.name2;
    console.log("++++++", ev, that)
    wx.setStorageSync("ow_number", ow_number), wx.setStorageSync("stu_number", stu_number), wx.navigateTo({
      url: "../cresumeReview/cresumeReview"
    })
  },

  feedback(ev) {
    var that = this;
    var e = ev.currentTarget.dataset.index;
    var ow_number = that.data.workinfo5[e].ow_number
    var stu_number = that.data.workinfo5[e].stu_number;
    console.log("++++++", ev, that)
    wx.navigateTo({
      url: "../cfeedback/cfeedback?ow_number=" + ow_number + '&stu_number=' + stu_number
    })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    app.editTabBar();
  },
  /*userlist(e) {
    var index = e.currentTarget.dataset.index;
    if (this.data.selectedFlag[index]){
      this.data.selectedFlag[index] = false;
    }else{
      this.data.selectedFlag[index] = true;
    }

    this.setData({
      selectedFlag: this.data.selectedFlag
    })
  },*/

  onRefresh() {
    //在当前页面显示导航条加载动画
    wx.showNavigationBarLoading();
    //显示 loading 提示框。需主动调用 wx.hideLoading 才能关闭提示框
    wx.showLoading({
      title: '刷新中...',
      duration: 1000
    })
    this.getData();
  },
  getData() {
    let that = this;
    that.setData({
      workinfo1: [],
      workinfo2: [],
      workinfo3: [],
      workinfo4: [],
      workinfo5: [],
    })
    wx.request({
      url: app.globalData.url + '/Show_applicant/',
      header: {
        'Content-Type': 'application/json'
      },
      method: "GET",
      data: {
        user: app.globalData.user
      },
      success: function (res) {
        console.log(res);
        var i;
        var baominger = []
        for (i = 0; i < res.data.length; i++) {
          if (res.statusCode == 200) {
            if (res.data[i].status == "待审核") {
              var baoming = {}
              var person = {}
              var count = 0
              if (that.data.workinfo1.length >= 1) {
                var m;
                for (m = 0; m < that.data.workinfo1.length; m++) {
                  if (res.data[i].ow_number == that.data.workinfo1[m].baominger[0].ow_number) {
                    baoming.ow_number = res.data[i].ow_number;
                    baoming.user = res.data[i].user;
                    baoming.stu_number = res.data[i].stu_number;
                    that.data.workinfo1[m].baominger.push(baoming)
                    that.setData({
                      workinfo1: that.data.workinfo1
                    })
                    break;
                  } else {
                    count = count + 1
                  }
                }
                if (count == that.data.workinfo1.length) {
                  var baominger2 = []
                  baoming.ow_number = res.data[i].ow_number;
                  baoming.user = res.data[i].user;
                  baoming.stu_number = res.data[i].stu_number;
                  baominger2.push(baoming)
                  person.post = res.data[i].post
                  person.baominger = baominger2
                  that.data.workinfo1.push(person)
                  that.setData({
                    workinfo1: that.data.workinfo1
                  })
                }
              } else {
                baoming.ow_number = res.data[i].ow_number;
                baoming.user = res.data[i].user;
                baoming.stu_number = res.data[i].stu_number;
                baominger.push(baoming)
                baominger = baominger
                person.post = res.data[i].post
                person.baominger = baominger
                that.data.workinfo1.push(person)
                that.setData({
                  workinfo1: that.data.workinfo1
                })
              }
              console.log(that.data.workinfo1)
            } else if (res.data[i].status == "表筛未通过") {
              that.data.workinfo2.push(res.data[i])
              that.setData({
                workinfo2: that.data.workinfo2
              })
            } else if (res.data[i].status == "未录用") {
              that.data.workinfo2.push(res.data[i])
              that.setData({
                workinfo2: that.data.workinfo2
              })
            } else if (res.data[i].status == "表筛通过") {
              that.data.workinfo3.push(res.data[i])
              that.setData({
                workinfo3: that.data.workinfo3
              })
            } else if (res.data[i].status == "面试中") {
              that.data.workinfo3.push(res.data[i])
              that.setData({
                workinfo3: that.data.workinfo3
              })
            } else if (res.data[i].status == "已录用") {
              that.data.workinfo4.push(res.data[i])
              that.setData({
                workinfo4: that.data.workinfo4
              })
            } else if (res.data[i].status == "工作结束") {
              that.data.workinfo5.push(res.data[i])
              that.setData({
                workinfo5: that.data.workinfo5
              })
            } else if (res.data[i].status == "待评价") {
              that.data.workinfo5.push(res.data[i])
              that.setData({
                workinfo5: that.data.workinfo5
              })
            } else if (res.data[i].status == "已评价") {
              that.data.workinfo5.push(res.data[i])
              that.setData({
                workinfo5: that.data.workinfo5
              })
            }
          }
        }
        //隐藏loading 提示框
        wx.hideLoading();
        //隐藏导航条加载动画
        wx.hideNavigationBarLoading();
        //停止下拉刷新
        wx.stopPullDownRefresh();
      }
    });

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
    this.onRefresh();
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})
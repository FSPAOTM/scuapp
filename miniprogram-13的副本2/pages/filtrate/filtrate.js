// pages/filtrate/filtrate.js
// index/list.js
Page({
 
  /**
   * 页面的初始数据
   */
  data: {
    tabTxt: ['类型', '综合排序', '区域'],//分类
    tab: [true, true, true],
    pinpaiList: [
      { 'id': '1', 'title': '家教' },
      { 'id': '2', 'title': '调研' },
      { 'id': '3', 'title': '服务员' },
      { 'id': '4', 'title': '实习' },
      { 'id': '5', 'title': '客服' },
      { 'id': '6', 'title': '安保' },
      { 'id': '7', 'title': '会展活动' },
      { 'id': '8', 'title': '代理' },
      { 'id': '9', 'title': '演出' },
      { 'id': '10', 'title': '送餐' },
      { 'id': '11', 'title': '摄影剪辑' },
      { 'id': '12', 'title': '翻译' },
      { 'id': '13', 'title': '设计' },
      { 'id': '14', 'title': '文案编辑' }
    ],

    pinpai_id: 0,//类型
    pinpai_txt: '',
    paixu_id: 0,//排序
    paixu_txt: '',
    xiaoliang_id: 0,//筛选
    xiaoliang_txt: '',
  
  details: [
    {
      salary: '100/天',
      settlement: '日结',
      company: 'XX公司',
      sex: '男女不限',
      title: 'XXX服务员',
      
    },
    {
      salary: '150/天',
      settlement: '完工结',
      company: 'XX公司',
      sex: '男女不限',
      title: 'XXX服务员',
    },
  ],
},



  // 选项卡
  filterTab: function (e) {
    var data = [true, true, true], index = e.currentTarget.dataset.index;
    data[index] = !this.data.tab[index];
    this.setData({
      tab: data
    })
  },

 
  //筛选项点击操作
  filter: function (e) {
    var self = this, id = e.currentTarget.dataset.id, txt = e.currentTarget.dataset.txt, tabTxt = this.data.tabTxt;
    switch (e.currentTarget.dataset.index) {
      case '0':
        tabTxt[0] = txt;
        self.setData({
          tab: [true, true, true],
          tabTxt: tabTxt,
          leixing_id: id,
          leixing_txt: txt
        });
        break;
      case '1':
        tabTxt[1] = txt;
        self.setData({
          tab: [true, true, true],
          tabTxt: tabTxt,
          paixu_id: id,
          paixu_txt: txt
        });
        break;
     
    }
    //数据筛选
    self.getDataList();
  },
 
  //加载数据
  getDataList: function () {
    //调用数据接口，获取数据
 
 
  },

  onReady: function () {
    this.animation = wx.createAnimation()
  },
  translate: function () {
    this.setData({
      isRuleTrue: true
    })
    this.animation.translate(-245, 0).step()
    this.setData({ animation: this.animation.export() })
  },

  success: function () {
    this.setData({
      isRuleTrue: false
    })
    this.animation.translate(0, 0).step()
    this.setData({ animation: this.animation.export() })
  },
  tryDriver: function () {
    this.setData({
      background: "#89dcf8"
    })
  }


})


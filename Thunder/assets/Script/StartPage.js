// Learn cc.Class:
//  - https://docs.cocos.com/creator/manual/en/scripting/class.html
// Learn Attribute:
//  - https://docs.cocos.com/creator/manual/en/scripting/reference/attributes.html
// Learn life-cycle callbacks:
//  - https://docs.cocos.com/creator/manual/en/scripting/life-cycle-callbacks.html

cc.Class({
    extends: cc.Component,

    properties: {
      button:cc.Button,
      SettingButton:cc.Button
    },

    // LIFE-CYCLE CALLBACKS:

    onLoad () {
       
        this.SettingButton.node.on("click",this.callback1,this)
        this.button.node.on("click",this.callback2,this)
    },

    callback1:function(button){
        cc.director.loadScene("Setting")
    },
    
    callback2:function(button){
        cc.director.loadScene("Game")
    },
    // start () {

    // },

    // update (dt) {},
});

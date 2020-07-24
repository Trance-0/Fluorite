// Learn cc.Class:
//  - https://docs.cocos.com/creator/manual/en/scripting/class.html
// Learn Attribute:
//  - https://docs.cocos.com/creator/manual/en/scripting/reference/attributes.html
// Learn life-cycle callbacks:
//  - https://docs.cocos.com/creator/manual/en/scripting/life-cycle-callbacks.html

cc.Class({
    extends: cc.Component,

    properties: {
      button:cc.Button

    },

    // LIFE-CYCLE CALLBACKS:

    onLoad () {
        // console.log(window.Global["score"]);
        this.button.node.on("click",this.callback,this)
    },

    callback:function(button){
        cc.director.loadScene("Game");
    },
    // start () {

    // },

    update (dt) {
        var score_label=this.node.getChildByName("Score");
        var showlabel=score_label.getComponent(cc.Label);
        showlabel.node._components[0].string="[ "+window.Global["score"]+" ]"
    },
});

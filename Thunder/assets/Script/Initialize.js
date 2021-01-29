// Learn cc.Class:
//  - https://docs.cocos.com/creator/manual/en/scripting/class.html
// Learn Attribute:
//  - https://docs.cocos.com/creator/manual/en/scripting/reference/attributes.html
// Learn life-cycle callbacks:
//  - https://docs.cocos.com/creator/manual/en/scripting/life-cycle-callbacks.html

cc.Class({
    extends: cc.Component,

    properties: {
    },

    // LIFE-CYCLE CALLBACKS:

    onLoad () {
        window.Global = {
            score: 0,
            autoFire:false,
            mobileMode:false,
            enemyFrequency:0.5
        };
    },

    start () {
        cc.director.loadScene("Start");
    },

    // update (dt) {},
});

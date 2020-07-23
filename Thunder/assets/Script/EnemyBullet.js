// Learn cc.Class:
//  - https://docs.cocos.com/creator/manual/en/scripting/class.html
// Learn Attribute:
//  - https://docs.cocos.com/creator/manual/en/scripting/reference/attributes.html
// Learn life-cycle callbacks:
//  - https://docs.cocos.com/creator/manual/en/scripting/life-cycle-callbacks.html

cc.Class({
    extends: cc.Component,

    properties: {
        // enemy:{
        //     default:null,
        //     type:cc.Sprite,
        // },
       speed:10,
    //    shootTime:2,
    },

    // // LIFE-CYCLE CALLBACKS:

    // // onLoad () {
    // //     this.node.lastShoot=0;
    // //     this.node.x=this.enemy.node.x;
    // //     this.node.y=this.enemy.node.y;
    // // },

    // // start () {

    // // },

    update (dt) {
        this.node.y-=this.speed;
    //     if (this.node.lastShoot>this.shootTime*60){
    //         this.node.x=this.enemy.node.x;
    //         this.node.y=this.enemy.node.y;
    //         this.node.lastShoot=0;
    //     }
    //     this.node.lastShoot+=1
    },
});

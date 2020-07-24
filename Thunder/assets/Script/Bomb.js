// Learn cc.Class:
//  - https://docs.cocos.com/creator/manual/en/scripting/class.html
// Learn Attribute:
//  - https://docs.cocos.com/creator/manual/en/scripting/reference/attributes.html
// Learn life-cycle callbacks:
//  - https://docs.cocos.com/creator/manual/en/scripting/life-cycle-callbacks.html

cc.Class({
    extends: cc.Component,

    properties: {
        // player:{
        //     default:null,
        //     type:cc.Sprite,
        // },
       speed:0.01,
    },

    // LIFE-CYCLE CALLBACKS:

    // onLoad () {
    //     this.node.lastShoot=0;
    //     this.node.x=this.player.node.x;
    //     this.node.y=this.player.node.y;
    // },

    start () {
        cc.director.getCollisionManager().enabled=true;
    },

    onCollisionEnter: function (other, self) {
        // console.log(other.node._name);
        // self.life-=1;
    },

    update (dt) {
        this.node.scale+=this.speed;
        if (this.node.scale>30){
            this.node.destroy();
        }
        // if (this.node.lastShoot>this.shootTime*60){
        //     this.node.x=this.player.node.x;
        //     this.node.y=this.player.node.y;
        //     this.node.lastShoot=0;
        // }
        // this.node.lastShoot+=1
    },
});

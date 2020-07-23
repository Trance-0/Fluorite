// Learn cc.Class:
//  - https://docs.cocos.com/creator/manual/en/scripting/class.html
// Learn Attribute:
//  - https://docs.cocos.com/creator/manual/en/scripting/reference/attributes.html
// Learn life-cycle callbacks:
//  - https://docs.cocos.com/creator/manual/en/scripting/life-cycle-callbacks.html

cc.Class({
    extends: cc.Component,

    properties: {

    // playerBullet:{
    //     default:null,
    //     type:cc.Sprite,
    // },
    // player:{
    //     default:null,
    //     type:cc.Sprite,
    // },
    xspeed:0.3,
    yspeed:0.3,
},



    // LIFE-CYCLE CALLBACKS:

    onLoad () {
        this.node.x=Math.random()*300-150;
        this.node.y=Math.random()*300;
        this.node.xs=this.xspeed;
        this.node.ys=this.yspeed;
    },

    start () {
        cc.director.getCollisionManager().enabled=true;
    },

    onCollisionEnter: function (other, self) {
        console.log('on collision enter');
        self.node.destroy();
    },
    // update (dt) {
        
        // if(Math.abs(this.playerBullet.node.x-this.node.x)<80){
        //     if(this.playerBullet.node.x>this.node.x){
        //         this.node.x-=this.node.xs;
        //     }
        //     else{
        //         this.node.x+=this.node.xs;
        //     }
        // }
        // else{
        //     if(this.playerBullet.node.x>this.node.x){
        //         this.node.x+=this.node.xs;
        //     }
        //     else{
        //         this.node.x-=this.node.xs;
        //     }
        // }

        // if(Math.abs(this.player.node.y-this.node.y)<80){
        //     if(this.player.node.y>this.node.y){
        //         this.node.y-=this.node.ys;
        //     }
        //     else{
        //         this.node.y+=this.node.ys;
        //     }
        // }
        // else{
        //     if(this.player.node.y>this.node.y){
        //         this.node.y+=this.node.ys;
        //     }
        //     else{
        //         this.node.y-=this.node.ys;
        //     }
        // }
//         if(this.bullet.node.y>this.node.y||this.bullet.node.y-this.node.y<-50){
//             this.node.ys=-this.yspeed;
//         }
//         if(this.bullet.node.y<this.node.y||this.bullet.node.y-this.node.y>50){
// this.node.ys=this.yspeed;
        // // }
        // if(this.node.x<-123){
        //     this.node.x=123;
        // }
        // if(this.node.x>121){
        //     this.node.x=121;
        // }
        // if(this.node.y<-283){
        //     this.node.y=283;
        // }
        // if(this.node.y>289){
        //     this.node.y=289;
        // }
        // console.log(this.node.x);
        // console.log(this.bullet.node.x);
    // },

});

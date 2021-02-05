// Learn cc.Class:
//  - https://docs.cocos.com/creator/manual/en/scripting/class.html
// Learn Attribute:
//  - https://docs.cocos.com/creator/manual/en/scripting/reference/attributes.html
// Learn life-cycle callbacks:
//  - https://docs.cocos.com/creator/manual/en/scripting/life-cycle-callbacks.html

cc.Class({
    extends: cc.Component,

    properties: {
       speed:10,
       life:3,
    },

    start () {
        cc.director.getCollisionManager().enabled=true;
    },

    onCollisionEnter: function (other, self) {
        // console.log(other.node._name);
        self.life-=1;
    },

    update (dt) {
        this.node.y+=this.speed;
        if (this.node.y>350||this.life<0){
            this.node.destroy();
            console.log("bulletDistroyed");
        }
    },
});

// Learn cc.Class:
//  - https://docs.cocos.com/creator/manual/en/scripting/class.html
// Learn Attribute:
//  - https://docs.cocos.com/creator/manual/en/scripting/reference/attributes.html
// Learn life-cycle callbacks:
//  - https://docs.cocos.com/creator/manual/en/scripting/life-cycle-callbacks.html

cc.Class({
    extends: cc.Component,
    
    properties: {
        ySpeed:5,
        xSpeed:10,
    },

    // LIFE-CYCLE CALLBACKS:

    onLoad () {

        this.node.xs=0;
        this.node.ys=0;
        // Initialize the keyboard input listening
        cc.systemEvent.on(cc.SystemEvent.EventType.KEY_DOWN, this.onKeyDown, this);
        cc.systemEvent.on(cc.SystemEvent.EventType.KEY_UP, this.onKeyUp, this);
    },

    start () {

    },

    update (dt) {
        if(this.node.x<-123){
            this.node.x=-123
        }
        if(this.node.x>121){
            this.node.x=121
        }
        if(this.node.y<-283){
            this.node.y=-283
        }
        if(this.node.y>289){
            this.node.y=289
        }
        this.node.y+=this.node.ys;
        this.node.x+=this.node.xs;

    },

    onKeyDown (event) {
        // set a flag when key pressed
        switch(event.keyCode) {
            case cc.macro.KEY.left:
                this.node.xs=-this.xSpeed;
                break;
            case cc.macro.KEY.right:
                this.node.xs=this.xSpeed;
                break;
            case cc.macro.KEY.up:
                this.node.ys=this.ySpeed;
                break;
            case cc.macro.KEY.down:
                this.node.ys=-this.ySpeed;
                break;
        }
    },

    onKeyUp (event) {
        // unset a flag when key released
        switch(event.keyCode) {
            case cc.macro.KEY.left:
                this.node.xs=0;
                break;
            case cc.macro.KEY.right:
                this.node.xs=0;
                break;
            case cc.macro.KEY.up:
                this.node.ys=0;
                break;
            case cc.macro.KEY.down:
                this.node.ys=0;
                    break;
        }
    },
    
});

// Learn cc.Class:
//  - https://docs.cocos.com/creator/manual/en/scripting/class.html
// Learn Attribute:
//  - https://docs.cocos.com/creator/manual/en/scripting/reference/attributes.html
// Learn life-cycle callbacks:
//  - https://docs.cocos.com/creator/manual/en/scripting/life-cycle-callbacks.html

cc.Class({
    extends: cc.Component,

    properties: {
        ySpeed: 5,
        xSpeed: 10,
        Life: 100,
        time: 0,
    },

    // LIFE-CYCLE CALLBACKS:

    onLoad() {
        this.node.Life = this.Life;
        this.node.xs = 0;
        this.node.ys = 0;
        // Initialize the keyboard input listening
        cc.systemEvent.on(cc.SystemEvent.EventType.KEY_DOWN, this.onKeyDown, this);
        cc.systemEvent.on(cc.SystemEvent.EventType.KEY_UP, this.onKeyUp, this);
        if(window.Global["mobileMode"]){
        this.node.on('touchmove', function (event) {

            if (event.getLocationX()-175 > this.node.x) {
                this.node.xs = this.xSpeed;
            }
            else if (event.getLocationX()-175 < this.node.x) {
                this.node.xs = -this.xSpeed;
            }
            else {
                this.node.xs = 0;
            }
            if (event.getLocationY()-320 > this.node.y) {
                this.node.ys = this.ySpeed;
            }
            else if (event.getLocationY()-320 < this.node.y) {
                this.node.ys = -this.ySpeed;
            }
            else {
                this.node.ys = 0;
            }

        }.bind(this));
        this.node.on('touchend', function (event) {
            this.node.xs = 0;
            this.node.ys = 0;
        }.bind(this));
        this.node.on('touchcancel', function (event) {
            this.node.xs = 0;
            this.node.ys = 0;
        }.bind(this));
    }
    },
    

    start() {
        cc.director.getCollisionManager().enabled = true;
    },

    onCollisionEnter: function (other, self) {
        if (other.node._name == "Enemy") {
            self.node.Life -= 10;
        }
        if (other.node._name == "enemy Bullet") {
            self.node.Life -= 1;
        }
    },

    update(dt) {

        if (this.node.Life < 0) {
            cc.director.loadScene("Gameover")
        }
        if (this.node.x < -175) {
            this.node.x = -175
        }
        if (this.node.x > 175) {
            this.node.x = 175
        }
        if (this.node.y < -325) {
            this.node.y = -325
        }
        if (this.node.y > 325) {
            this.node.y = 325
        }
        this.node.y += this.node.ys;
        this.node.x += this.node.xs;

    },

    onKeyDown(event) {
        // set a flag when key pressed
        switch (event.keyCode) {
            case cc.macro.KEY.left:
                this.node.xs = -this.xSpeed;
                break;
            case cc.macro.KEY.right:
                this.node.xs = this.xSpeed;
                break;
            case cc.macro.KEY.up:
                this.node.ys = this.ySpeed;
                break;
            case cc.macro.KEY.down:
                this.node.ys = -this.ySpeed;
                break;
        }
    },

    onKeyUp(event) {
        // unset a flag when key released
        switch (event.keyCode) {
            case cc.macro.KEY.left:
                this.node.xs = 0;
                break;
            case cc.macro.KEY.right:
                this.node.xs = 0;
                break;
            case cc.macro.KEY.up:
                this.node.ys = 0;
                break;
            case cc.macro.KEY.down:
                this.node.ys = 0;
                break;
        }
    },

});

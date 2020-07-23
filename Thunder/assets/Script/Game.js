// Learn cc.Class:
//  - https://docs.cocos.com/creator/manual/en/scripting/class.html
// Learn Attribute:
//  - https://docs.cocos.com/creator/manual/en/scripting/reference/attributes.html
// Learn life-cycle callbacks:
//  - https://docs.cocos.com/creator/manual/en/scripting/life-cycle-callbacks.html

cc.Class({
    extends: cc.Component,

    properties: {
        enemyPF: {
            default: null,
            type: cc.Prefab
        },
        enemies: {
            default: [],
            type: cc.Sprite
        },
        player: {
            default: null,
            type: cc.Sprite
        },

        playerBulletPF: {
            default: null,
            type: cc.Prefab
        },
        enemyBulletPF: {
            default: null,
            type: cc.Prefab
        },
        ememyBulletFrequecy:100000,
        time:0
    },

    // LIFE-CYCLE CALLBACKS:

    onLoad() {
        for (i = 0; i < 10; i++) {
            var enemy = cc.instantiate(this.enemyPF);
            this.enemies.push(enemy);
            this.node.addChild(this.enemies[this.enemies.length - 1]);
        }
        console.log(this.enemies);
        cc.systemEvent.on(cc.SystemEvent.EventType.KEY_DOWN, this.onKeyDown, this);

    },

    // spawnEnemy(){
    //     var newEnemy=cc.instantiate(this.enemyPF);
    //     this.node.addChild(newEnemy);
    // },

    start() {
        // for (i=0;i<10;i++){
        //     this.spawnEnemy();
        // }
    },


    onKeyDown(event) {
        // set a flag when key pressed
        switch (event.keyCode) {
            case cc.macro.KEY.space:
                var newbullet = cc.instantiate(this.playerBulletPF);
                newbullet.setPosition(this.player.node.x, this.player.node.y);
                this.node.addChild(newbullet);
                break;
        }
    },

    ClearNullArr(arr){
        for(var i=0,len=arr.length;i<len;i++){
        if(arr[i]._objFlags!=0){
            arr.splice(i,1);
            len--;
            i--;
            }
            }
        return arr;
        },

    update(dt) {
        this.enemies=this.ClearNullArr(this.enemies);

        console.log(this.enemies);
        if (this.time>this.ememyBulletFrequecy){
            for(i=0;i<this.enemies.length;i++){
                var newbullet = cc.instantiate(this.enemyBulletPF);
                newbullet.setPosition(this.enemies[i].x, this.enemies[i].y);
                this.node.addChild(newbullet);
            }
            this.time=0;
        }
        this.time+=1;
        for (i = 0; i < this.enemies.length; i++) {
            for (j=0;j<this.enemies.length;j++){
                if (j!=i&&Math.pow(this.enemies[j].x-this.enemies[i].x,2)+Math.pow(this.enemies[j].y-this.enemies[i].y,2)<2500){
                    if (Math.abs(this.enemies[j].x - this.enemies[i].x) < 60) {
                        if (this.enemies[j].x > this.enemies[i].x) {
                            this.enemies[i].x -= this.enemies[i].xs;
                        }
                        else {
                            this.enemies[i].x += this.enemies[i].xs;
                        }
                    }
                    if (Math.abs(this.enemies[j].y - this.enemies[i].y) < 60) {
                        if (this.enemies[j].y > this.enemies[i].y) {
                            this.enemies[i].y -= this.enemies[i].ys;
                        }
                        else {
                            this.enemies[i].y += this.enemies[i].ys;
                        }
                    }
                }
            }
            if (Math.abs(this.player.node.x - this.enemies[i].x) < 80) {
                if (this.player.node.x > this.enemies[i].x) {
                    this.enemies[i].x -= this.enemies[i].xs;
                }
                else {
                    this.enemies[i].x += this.enemies[i].xs;
                }
            }
            else {
                if (this.player.node.x > this.enemies[i].x) {
                    this.enemies[i].x += this.enemies[i].xs;
                }
                else {
                    this.enemies[i].x -= this.enemies[i].xs;
                }
            }

            if (Math.abs(this.player.node.y - this.enemies[i].y) < 80) {
                if (this.player.node.y > this.enemies[i].y) {
                    this.enemies[i].y -= this.enemies[i].ys;
                }
                else {
                    this.enemies[i].y += this.enemies[i].ys;
                }
            }
            else {
                if (this.player.node.y > this.enemies[i].y) {
                    this.enemies[i].y += this.enemies[i].ys;
                }
                else {
                    this.enemies[i].y -= this.enemies[i].ys;
                }
            }
            if (this.enemies[i].x < -123) {
                this.enemies[i].x = -123;
            }
            if (this.enemies[i].x > 121) {
                this.enemies[i].x = 121;
            }
            if (this.enemies[i].y < -283) {
                this.enemies[i].y = -283;
            }
            if (this.enemies[i].y > 289) {
                this.enemies[i].y = 289;
            }
        }
    },
});

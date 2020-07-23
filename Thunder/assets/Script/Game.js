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
        playerBullets: {
            default: [],
            type: cc.Sprite
        },
        player: {
            default: null,
            type: cc.Sprite
        },
        LifeBar: {
            default: null,
            type: cc.Sprite
        },
        EnergyBar: {
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
        ememyBulletFrq: 100000,
        enemyFrq: 5,
        time: 0,
        warningDistance: 100,
    },

    // LIFE-CYCLE CALLBACKS:

    onLoad() {
        window.Global = {
            score: 0
        };
        this.schedule(function () {
            var enemy = cc.instantiate(this.enemyPF);
            this.enemies.push(enemy);
            this.node.addChild(this.enemies[this.enemies.length - 1]);
        }, this.enemyFrq);
        this.node.LifeBar = this.LifeBar;
        // console.log(this.enemies);
        cc.systemEvent.on(cc.SystemEvent.EventType.KEY_DOWN, this.onKeyDown, this);

    },

    // spawnEnemy(){
    //     var newEnemy=cc.instantiate(this.enemyPF);
    //     this.node.addChild(newEnemy);
    // },

    start() {
        console.log(cc.find("Score"));
        this.node.score = this.score;
    },


    onKeyDown(event) {
        // set a flag when key pressed
        switch (event.keyCode) {
            case cc.macro.KEY.space:
                var newbullet = cc.instantiate(this.playerBulletPF);
                newbullet.setPosition(this.player.node.x, this.player.node.y);
                this.playerBullets.push(newbullet);
                this.node.addChild(this.playerBullets[this.playerBullets.length - 1]);
                break;
        }
    },


    ClearNullArr(arr) {
        for (var i = 0, len = arr.length; i < len; i++) {
            if (arr[i]._objFlags != 0) {
                arr.splice(i, 1);
                len--;
                i--;
            }
        }
        return arr;
    },

    update(dt) {
        this.enemies = this.ClearNullArr(this.enemies);
        this.playerBullets = this.ClearNullArr(this.playerBullets);

        this.node.LifeBar.node._components[0].node._components[1].progress = this.player.node.Life / 100;
        // console.log(this.node.LifeBar.node._components[0].node._components[1].progress);
        // console.log(this.enemies);
        if (this.time > this.ememyBulletFrq) {
            for (i = 0; i < this.enemies.length; i++) {
                var newbullet = cc.instantiate(this.enemyBulletPF);
                newbullet.setPosition(this.enemies[i].x, this.enemies[i].y);
                this.node.addChild(newbullet);
            }
            this.time = 0;
        }
        this.time += 1;
        for (i = 0; i < this.enemies.length; i++) {
            for (j = 0; j < this.enemies.length; j++) {
                if (j != i && Math.pow(this.enemies[j].x - this.enemies[i].x, 2) + Math.pow(this.enemies[j].y - this.enemies[i].y, 2) < 2500) {
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


            console.log(this.playerBullets);
            for (j = 0; j < this.playerBullets.length; j++) {
                if (Math.abs(this.playerBullets[j].x - this.enemies[i].x) < this.warningDistance) {
                    if (this.playerBullets[j].x > this.enemies[i].x) {
                        this.enemies[i].x -= this.enemies[i].xs;
                    }
                    else {
                        this.enemies[i].x += this.enemies[i].xs;
                    }
                }
            }


            if (Math.abs(this.player.node.y - this.enemies[i].y) < this.warningDistance) {
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

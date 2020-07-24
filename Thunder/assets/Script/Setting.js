// Learn cc.Class:
//  - https://docs.cocos.com/creator/manual/en/scripting/class.html
// Learn Attribute:
//  - https://docs.cocos.com/creator/manual/en/scripting/reference/attributes.html
// Learn life-cycle callbacks:
//  - https://docs.cocos.com/creator/manual/en/scripting/life-cycle-callbacks.html

cc.Class({
    extends: cc.Component,
    properties: {
        button:cc.Button,
        toggle:cc.Toggle,
      },
  
      // LIFE-CYCLE CALLBACKS:
  
      onLoad () {
          // console.log(window.Global["score"]);
          
          this.button.node.on("click",this.callback,this)
      },
  
      callback:function(button){
        window.Global["Auto_fire"]=this.node.getChildByName("toggle").getComponent(cc.Toggle).isChecked;
        cc.director.loadScene("StartPage");
        console.log(window.Global["Auto_fire"]);
      },
      // start () {
  
      // },
  
      update (dt) {

        //   console.log(this.node)
      },
});

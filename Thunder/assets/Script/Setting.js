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
        autoFire:cc.Toggle,
        mobileMode:cc.Toggle,
      },
  
      // LIFE-CYCLE CALLBACKS:
  
      onLoad () {
          // console.log(3.Global["score"]);
          
          this.button.node.on("click",this.callback,this)
      },
  
      callback:function(button){
        // console.log(this.node)
        window.Global["mobileMode"]=this.node.getChildByName("mobileMode")._components[0].isChecked;
        console.log(this.node.getChildByName("mobileMode")._components[0].isChecked)
        window.Global["autoFire"]=this.node.getChildByName("autoFire")._components[0].isChecked;
        console.log(this.node.getChildByName("autoFire")._components[0].isChecked)
        cc.director.loadScene("StartPage");
        // console.log(window.Global["Auto_fire"]);
      },
      // start () {
  
      // },
  
      update (dt) {
        if(this.node.getChildByName("mobileMode")._components[0].isChecked){
          this.node.getChildByName("autoFire")._components[0].isChecked=true;
        }
        //   console.log(this.node)
      },
});


using Bridge;
using System;
        
        
namespace FVTTBridge.Bindings
{
        
    [External]
    [Namespace(false)]    
    public class MeasuredTemplate{
       public dynamic shape;
       public dynamic template;
       public dynamic _borderThickness;
       public dynamic ruler;
       public dynamic texture;
       public dynamic controlIcon;
       public dynamic embeddedName(){return null;}//dummy return
       public dynamic borderColor(){return null;}//dummy return
       public dynamic fillColor(){return null;}//dummy return
       public dynamic owner(){return null;}//dummy return
       public dynamic draw(){return null;}//dummy return
       public dynamic _drawControlIcon(){return null;}//dummy return
       public dynamic _drawRulerText(){return null;}//dummy return
       public dynamic refresh(){return null;}//dummy return
       public dynamic _getCircleShape(dynamic distance){return null;}//dummy return
       public dynamic _getConeShape(dynamic direction, dynamic angle, dynamic distance){return null;}//dummy return
       public dynamic _getRectShape(dynamic direction, dynamic distance){return null;}//dummy return
       public dynamic _getRayShape(dynamic direction, dynamic distance, dynamic width){return null;}//dummy return
       public dynamic _drawRotationHandle(dynamic radius){return null;}//dummy return
       public dynamic _refreshRulerText(){return null;}//dummy return
       public dynamic highlightGrid(){return null;}//dummy return
       public dynamic rotate(dynamic angle, dynamic snap){return null;}//dummy return
       public dynamic _canControl(dynamic user, dynamic event){return null;}//dummy return
       public dynamic _canConfigure(dynamic user, dynamic event){return null;}//dummy return
       public dynamic _canView(dynamic user, dynamic event){return null;}//dummy return
       public dynamic _onUpdate(dynamic data){return null;}//dummy return
       public dynamic _onDelete(){return null;}//dummy return

    }
        
}
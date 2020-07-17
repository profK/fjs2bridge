
using Bridge;
using System;
        
        
namespace FVTTBridge.Bindings
{
        
    [External]
    [Namespace(false)]    
    public class ControlIcon{
       public dynamic interactive;
       public dynamic border;
       public dynamic bg;
       public dynamic rect;
       public dynamic hitArea;
       public dynamic borderColor;
       public dynamic tintColor;
       public dynamic texture;
       public dynamic interactiveChildren;
       public dynamic icon;
       public dynamic size;
       public dynamic draw(){return null;}//dummy return
       public dynamic _onHoverIn(dynamic event){return null;}//dummy return
       public dynamic _onHoverOut(dynamic event){return null;}//dummy return

    }
        
}

using Bridge;
using System;
        
        
namespace FVTTBridge.Bindings
{
        
    [External]
    [Namespace(false)]    
    public class ContextMenu{
       public ContextMenu(dynamic element, dynamic selector, dynamic menuItems, dynamic optionsObject){}//dummy body
       public dynamic element;
       public dynamic _expandUp;
       public dynamic eventName;
       public dynamic menuItems;
       public dynamic selector;
       public dynamic menu(){return null;}//dummy return
       public dynamic bind(){return null;}//dummy return
       public dynamic close(){return null;}//dummy return
       public dynamic _animateOpen(dynamic menu){return null;}//dummy return
       public dynamic _animateClose(dynamic menu){return null;}//dummy return
       public dynamic render(dynamic target){return null;}//dummy return
       public dynamic _setPosition(dynamic html, dynamic target){return null;}//dummy return
       public dynamic eventListeners(){return null;}//dummy return

    }
        
}
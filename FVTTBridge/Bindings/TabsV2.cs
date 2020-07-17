
using Bridge;
using System;
        
        
namespace FVTTBridge.Bindings
{
        
    [External]
    [Namespace(false)]    
    public class TabsV2{
       public dynamic _content;
       public dynamic _nav;
       public dynamic callback;
       public dynamic _navSelector;
       public dynamic _contentSelector;
       public dynamic active;
       public dynamic bind(dynamic html){return null;}//dummy return
       public dynamic activate(dynamic tabName, optionsObject){return null;}//dummy return
       public dynamic _onClickNav(dynamic event){return null;}//dummy return

    }
        
}
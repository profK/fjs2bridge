
using Bridge;
using System;
        
        
namespace FVTTBridge.Bindings
{
        
    [External]
    [Namespace(false)]    
    public class Tabs{
       public Tabs(dynamic tabs, dynamic optionsObject){}//dummy body
       public dynamic callback;
       public dynamic tabs;
       public dynamic container;
       public dynamic tab;
       public dynamic active;
       public dynamic group(){return null;}//dummy return
       public dynamic activateTab(dynamic tab){return null;}//dummy return

    }
        
}
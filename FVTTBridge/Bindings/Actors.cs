
using Bridge;
using System;
        
        
namespace FVTTBridge.Bindings
{
        
    [External]
    [Namespace(false)]    
    public class Actors{
       public dynamic tokens;
       public dynamic object(){return null;}//dummy return
       public static void registerSheet(params dynamic[] sheets){}
       public dynamic unregisterSheet(params dynamic[] args){return null;}//dummy return
       public dynamic registeredSheets(){return null;}//dummy return

    }
        
}
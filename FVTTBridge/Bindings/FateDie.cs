
using Bridge;
using System;
        
        
namespace FVTTBridge.Bindings
{
        
    [External]
    [Namespace(false)]    
    public class FateDie{
       public FateDie(){}//dummy body
       public dynamic sides;
       public dynamic _getTooltip(dynamic result){return null;}//dummy return

    }
        
}
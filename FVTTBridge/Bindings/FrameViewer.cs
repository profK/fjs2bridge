
using Bridge;
using System;
        
        
namespace FVTTBridge.Bindings
{
        
    [External]
    [Namespace(false)]    
    public class FrameViewer{
       public FrameViewer(dynamic url, dynamic options){}//dummy body
       public dynamic url;
       public dynamic defaultOptions(){return null;}//dummy return
       public dynamic getData(){return null;}//dummy return
       public dynamic close(){return null;}//dummy return

    }
        
}
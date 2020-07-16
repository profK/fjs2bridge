
using Bridge;
using System;
        
        
namespace FVTTBridge.Bindings
{
        
    [External]
    [Namespace(false)]    
    public class AudioHelper{
       public dynamic _analyserStreams;
       public dynamic _audioContext;
       public dynamic pending;
       public dynamic locked;
       public dynamic _analyserInterval;
       public dynamic sounds;
       public dynamic _fftArray;

    }
        
}
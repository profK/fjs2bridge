
using Bridge;
using System;
        
        
namespace FVTTBridge.Bindings
{
        
    [External]
    [Namespace(false)]    
    public class AudioHelper{
       public dynamic _analyserStreams;
       public dynamic _fftArray;
       public dynamic locked;
       public dynamic _analyserInterval;
       public dynamic pending;
       public dynamic _audioContext;
       public dynamic sounds;
       public dynamic registerSettings();
       public dynamic create(optionsObject);
       public dynamic play(dynamic src, dynamic id);
       public dynamic awaitFirstGesture();
       public dynamic _onFirstGesture(dynamic event);
       public dynamic preload(dynamic data);
       public dynamic socketListeners(dynamic socket);
       public dynamic play(dynamic data, dynamic push);
       public dynamic preload(dynamic data);
       public dynamic inputToVolume(dynamic value, dynamic order);
       public dynamic volumeToInput(dynamic volume, dynamic order);
       public dynamic hasAudioExtension(dynamic src);
       public dynamic getAudioContext();
       public dynamic startLevelReports(dynamic id, dynamic stream, dynamic callback, dynamic interval, dynamic smoothing);
       public dynamic stopLevelReports(dynamic id);
       public dynamic _ensureAnalyserTimer();
       public dynamic _cancelAnalyserTimer();
       public dynamic _emitVolumes();

    }
        
}
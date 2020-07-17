
using Bridge;
using System;
        
        
namespace FVTTBridge.Bindings
{
        
    [External]
    [Namespace(false)]    
    public class SightLayer{
       public dynamic _fogUpdated;
       public dynamic _initialized;
       public dynamic sources;
       public dynamic _cull;
       public dynamic _fogUpdates;
       public dynamic _fogResolution;
       public dynamic _blurDistance;
       public dynamic fogData;
       public dynamic alphas;
       public dynamic _channels;
       public dynamic tokenVision(){return null;}//dummy return
       public dynamic fogExploration(){return null;}//dummy return
       public dynamic blurDistance(){return null;}//dummy return
       public dynamic blurDistance(dynamic d){return null;}//dummy return
       public dynamic tearDown(){return null;}//dummy return
       public dynamic initialize(){return null;}//dummy return
       public dynamic initializeLights(optionsObject){return null;}//dummy return
       public dynamic initializeTokens(optionsObject){return null;}//dummy return
       public dynamic initializeFog(){return null;}//dummy return
       public dynamic updateLight(dynamic light, optionsObject){return null;}//dummy return
       public dynamic updateToken(dynamic token, optionsObject){return null;}//dummy return
       public dynamic draw(){return null;}//dummy return
       public dynamic _drawFogContainer(){return null;}//dummy return
       public dynamic _drawLightContainer(){return null;}//dummy return
       public dynamic _drawSource(dynamic hex, optionsObject){return null;}//dummy return
       public dynamic _createFogStagingTexture(){return null;}//dummy return
       public dynamic update(){return null;}//dummy return
       public dynamic restrictVisibility(){return null;}//dummy return
       public dynamic loadFog(){return null;}//dummy return
       public dynamic resetFog(){return null;}//dummy return
       public dynamic saveFog(){return null;}//dummy return
       public dynamic updateFog(dynamic x, dynamic y, dynamic radius, dynamic limit, dynamic force){return null;}//dummy return
       public dynamic computeSight(dynamic origin, dynamic radius, optionsObject){return null;}//dummy return
       public dynamic testVisibility(dynamic point, optionsObject){return null;}//dummy return
       public dynamic _configureBlurDistance(){return null;}//dummy return
       public dynamic _configureChannels(){return null;}//dummy return
       public dynamic _configureCullThreshold(){return null;}//dummy return
       public dynamic _configureFogResolution(){return null;}//dummy return
       public dynamic _createShadowMapFilter(){return null;}//dummy return
       public dynamic _castSightRays(dynamic x, dynamic y, dynamic distance, dynamic cullDistance, dynamic radialDensity, dynamic limitAngle, dynamic aMin, dynamic aMax){return null;}//dummy return
       public dynamic _adjustRayAngle(dynamic aMin, dynamic angle){return null;}//dummy return
       public dynamic _createOrUpdateFogExploration(dynamic fogData){return null;}//dummy return
       public dynamic _commitFogUpdate(){return null;}//dummy return
       public dynamic _onResetFog(dynamic resetData){return null;}//dummy return
       public dynamic setDebug(){return null;}//dummy return

    }
        
}
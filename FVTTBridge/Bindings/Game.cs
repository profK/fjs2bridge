
using Bridge;
using System;
        
        
namespace FVTTBridge.Bindings
{
        
    [External]
    [Namespace(false)]    
    public class Game{
       public dynamic keyboard;
       public dynamic i18n;
       public dynamic modules;
       public dynamic socket;
       public dynamic data;
       public dynamic audio;
       public dynamic settings;
       public dynamic debug;
       public dynamic loading;
       public dynamic video;
       public dynamic ready;
       public dynamic sessionId;
       public dynamic userId;
       public dynamic permissions;
       public dynamic create(){return null;}//dummy return
       public dynamic connect(dynamic sessionId){return null;}//dummy return
       public dynamic getCookies(){return null;}//dummy return
       public dynamic getWorldData(dynamic socket){return null;}//dummy return
       public dynamic getSetupData(dynamic socket){return null;}//dummy return
       public dynamic initialize(){return null;}//dummy return
       public dynamic _displayUsabilityErrors(){return null;}//dummy return
       public dynamic shutDown(){return null;}//dummy return
       public dynamic setupGame(){return null;}//dummy return
       public dynamic initializeEntities(){return null;}//dummy return
       public dynamic initializePacks(dynamic config){return null;}//dummy return
       public dynamic initializeRTC(){return null;}//dummy return
       public dynamic initializeUI(){return null;}//dummy return
       public dynamic initializeCanvas(){return null;}//dummy return
       public dynamic initializeKeyboard(){return null;}//dummy return
       public dynamic registerSettings(){return null;}//dummy return
       public dynamic isAdmin(){return null;}//dummy return
       public dynamic user(){return null;}//dummy return
       public dynamic world(){return null;}//dummy return
       public dynamic system(){return null;}//dummy return
       public dynamic combat(){return null;}//dummy return
       public dynamic paused(){return null;}//dummy return
       public dynamic activeTool(){return null;}//dummy return
       public dynamic togglePause(dynamic pause, dynamic push){return null;}//dummy return
       public dynamic logOut(){return null;}//dummy return
       public dynamic openSockets(){return null;}//dummy return
       public dynamic socketListeners(dynamic socket){return null;}//dummy return
       public dynamic activateListeners(){return null;}//dummy return
       public dynamic _onBeforeUnload(dynamic event){return null;}//dummy return
       public dynamic _onClickHyperlink(dynamic event){return null;}//dummy return
       public dynamic _onPreventDragstart(dynamic event){return null;}//dummy return
       public dynamic _onPreventDragover(dynamic event){return null;}//dummy return
       public dynamic _onPreventDrop(dynamic event){return null;}//dummy return
       public dynamic _onResize(dynamic event){return null;}//dummy return
       public dynamic _initializeGameView(){return null;}//dummy return
       public dynamic _initializeLicenseView(){return null;}//dummy return
       public dynamic _initializeSetupView(){return null;}//dummy return
       public dynamic _initializeJoinView(){return null;}//dummy return
       public dynamic _onJoinFormSubmit(dynamic event){return null;}//dummy return
       public dynamic _initializeStreamView(){return null;}//dummy return
       public dynamic _initializePlayersView(){return null;}//dummy return

    }
        
}
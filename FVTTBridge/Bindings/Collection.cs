
using Bridge;
using System;
        
        
namespace FVTTBridge.Bindings
{
        
    [External]
    [Namespace(false)]    
    public class Collection{
       public dynamic this[int i]{get;set;}
       public dynamic entries();
       public dynamic find(dynamic condition);
       public dynamic filter(dynamic condition);
       public dynamic get(dynamic key, optionsObject);
       public dynamic map(dynamic transformer);
       public dynamic reduce(dynamic evaluator, dynamic initial);

    }
        
}
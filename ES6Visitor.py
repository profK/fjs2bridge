class ES6Visitor:
    def __init__(self):
        self.indent=""
    
    def EnterNode(self,name):
        self.Print("Entering "+name)
        self.indent = self.indent+"    "

    def ExitNode(self,name):
        self.indent = self.indent[:len(self.indent)-4]
        self.Print("Exiting "+name)
        
    def Print(self,text):
        print(self.indent+text)
        
    def DoEnterProgram(self,node):
        self.EnterNode("Program")
    def DoExitProgram(self,node):
        self.ExitNode("Program")
    def DoProgram(self,node):
        self.Print("type:"+str(node.type))
        self.Print("sourceType:"+str(node.sourceType))
        for subnode in node.body:
            self.Visit(subnode)
    def DoEnterExpressionStatement(self,node):
        self.EnterNode("ExpressionStatement")
    def DoExitExpressionStatement(self,node):
        self.ExitNode("ExpressionStatement")
    def DoExpressionStatement(self,node):
        self.Print("type:"+str(node.type))
        self.Visit(node.expression)
    def DoEnterAssignmentExpression(self,node):
        self.EnterNode("AssignmentExpression")
    def DoExitAssignmentExpression(self,node):
        self.ExitNode("AssignmentExpression")
    def DoAssignmentExpression(self,node):
        self.Print("type:"+str(node.type))
        self.Print("operator:"+str(node.operator))
        self.Visit(node.left)
        self.Visit(node.right)
    def DoEnterIdentifier(self,node):
        self.EnterNode("Identifier")
    def DoExitIdentifier(self,node):
        self.ExitNode("Identifier")
    def DoIdentifier(self,node):
        self.Print("type:"+str(node.type))
        self.Print("name:"+str(node.name))
    def DoEnterMemberExpression(self,node):
        self.EnterNode("MemberExpression")
    def DoExitMemberExpression(self,node):
        self.ExitNode("MemberExpression")
    def DoMemberExpression(self,node):
        self.Print("type:"+str(node.type))
        self.Print("computed:"+str(node.computed))
        self.Visit(node.object)
        self.Visit(node.property)
    def DoEnterVariableDeclaration(self,node):
        self.EnterNode("VariableDeclaration")
    def DoExitVariableDeclaration(self,node):
        self.ExitNode("VariableDeclaration")
    def DoVariableDeclaration(self,node):
        self.Print("type:"+str(node.type))
        for subnode in node.declarations:
            self.Visit(subnode)
        self.Print("kind:"+str(node.kind))
    def DoEnterVariableDeclarator(self,node):
        self.EnterNode("VariableDeclarator")
    def DoExitVariableDeclarator(self,node):
        self.ExitNode("VariableDeclarator")
    def DoVariableDeclarator(self,node):
        self.Print("type:"+str(node.type))
        self.Visit(node.id)
        self.Visit(node.init)
    def DoEnterObjectExpression(self,node):
        self.EnterNode("ObjectExpression")
    def DoExitObjectExpression(self,node):
        self.ExitNode("ObjectExpression")
    def DoObjectExpression(self,node):
        self.Print("type:"+str(node.type))
        for subnode in node.properties:
            self.Visit(subnode)
    def DoEnterProperty(self,node):
        self.EnterNode("Property")
    def DoExitProperty(self,node):
        self.ExitNode("Property")
    def DoProperty(self,node):
        self.Print("type:"+str(node.type))
        self.Visit(node.key)
        self.Print("computed:"+str(node.computed))
        self.Visit(node.value)
        self.Print("kind:"+str(node.kind))
        self.Print("method:"+str(node.method))
        self.Print("shorthand:"+str(node.shorthand))
    def DoEnterClassDeclaration(self,node):
        self.EnterNode("ClassDeclaration")
    def DoExitClassDeclaration(self,node):
        self.ExitNode("ClassDeclaration")
    def DoClassDeclaration(self,node):
        self.Print("type:"+str(node.type))
        self.Visit(node.id)
        self.Visit(node.superClass)
        self.Visit(node.body)
    def DoEnterClassBody(self,node):
        self.EnterNode("ClassBody")
    def DoExitClassBody(self,node):
        self.ExitNode("ClassBody")
    def DoClassBody(self,node):
        self.Print("type:"+str(node.type))
        for subnode in node.body:
            self.Visit(subnode)
    def DoEnterMethodDefinition(self,node):
        self.EnterNode("MethodDefinition")
    def DoExitMethodDefinition(self,node):
        self.ExitNode("MethodDefinition")
    def DoMethodDefinition(self,node):
        self.Print("type:"+str(node.type))
        self.Visit(node.key)
        self.Print("computed:"+str(node.computed))
        self.Visit(node.value)
        self.Print("kind:"+str(node.kind))
        self.Print("static:"+str(node.static))
    def DoEnterFunctionExpression(self,node):
        self.EnterNode("FunctionExpression")
    def DoExitFunctionExpression(self,node):
        self.ExitNode("FunctionExpression")
    def DoFunctionExpression(self,node):
        self.Print("type:"+str(node.type))
        self.Print("expression:"+str(node.expression))
        self.Print("isAsync:"+str(node.isAsync))
        for subnode in node.params:
            self.Visit(subnode)
        self.Visit(node.body)
        self.Print("generator:"+str(node.generator))
    def DoEnterBlockStatement(self,node):
        self.EnterNode("BlockStatement")
    def DoExitBlockStatement(self,node):
        self.ExitNode("BlockStatement")
    def DoBlockStatement(self,node):
        self.Print("type:"+str(node.type))
        for subnode in node.body:
            self.Visit(subnode)
    def DoEnterForOfStatement(self,node):
        self.EnterNode("ForOfStatement")
    def DoExitForOfStatement(self,node):
        self.ExitNode("ForOfStatement")
    def DoForOfStatement(self,node):
        self.Print("type:"+str(node.type))
        self.Visit(node.left)
        self.Visit(node.right)
        self.Visit(node.body)
    def DoEnterCallExpression(self,node):
        self.EnterNode("CallExpression")
    def DoExitCallExpression(self,node):
        self.ExitNode("CallExpression")
    def DoCallExpression(self,node):
        self.Print("type:"+str(node.type))
        self.Visit(node.callee)
        for subnode in node.arguments:
            self.Visit(subnode)
    def DoEnterIfStatement(self,node):
        self.EnterNode("IfStatement")
    def DoExitIfStatement(self,node):
        self.ExitNode("IfStatement")
    def DoIfStatement(self,node):
        self.Print("type:"+str(node.type))
        self.Visit(node.test)
        self.Visit(node.consequent)
    def DoEnterBinaryExpression(self,node):
        self.EnterNode("BinaryExpression")
    def DoExitBinaryExpression(self,node):
        self.ExitNode("BinaryExpression")
    def DoBinaryExpression(self,node):
        self.Print("type:"+str(node.type))
        self.Print("operator:"+str(node.operator))
        self.Visit(node.left)
        self.Visit(node.right)
    def DoEnterFunctionDeclaration(self,node):
        self.EnterNode("FunctionDeclaration")
    def DoExitFunctionDeclaration(self,node):
        self.ExitNode("FunctionDeclaration")
    def DoFunctionDeclaration(self,node):
        self.Print("type:"+str(node.type))
        self.Print("generator:"+str(node.generator))
        self.Print("expression:"+str(node.expression))
        self.Print("isAsync:"+str(node.isAsync))
        self.Visit(node.id)
        for subnode in node.params:
            self.Visit(subnode)
        self.Visit(node.body)
    def DoEnterAssignmentPattern(self,node):
        self.EnterNode("AssignmentPattern")
    def DoExitAssignmentPattern(self,node):
        self.ExitNode("AssignmentPattern")
    def DoAssignmentPattern(self,node):
        self.Print("type:"+str(node.type))
        self.Visit(node.left)
        self.Visit(node.right)
    def DoEnterObjectPattern(self,node):
        self.EnterNode("ObjectPattern")
    def DoExitObjectPattern(self,node):
        self.ExitNode("ObjectPattern")
    def DoObjectPattern(self,node):
        self.Print("type:"+str(node.type))
        for subnode in node.properties:
            self.Visit(subnode)
    def DoEnterTryStatement(self,node):
        self.EnterNode("TryStatement")
    def DoExitTryStatement(self,node):
        self.ExitNode("TryStatement")
    def DoTryStatement(self,node):
        self.Print("type:"+str(node.type))
        self.Visit(node.block)
        self.Visit(node.handler)
    def DoEnterCatchClause(self,node):
        self.EnterNode("CatchClause")
    def DoExitCatchClause(self,node):
        self.ExitNode("CatchClause")
    def DoCatchClause(self,node):
        self.Print("type:"+str(node.type))
        self.Visit(node.param)
        self.Visit(node.body)

    def DoEnterNone(self,node):
        self.EnterNode("None")
    def DoNone(self,node):
        self.Print("Found none value")
    def DoExitNone(self,node):
        self.ExitNode("CatchClause")


    def Visit(self,node):
     if (node == None):
         self.DoEnterNone(node)
         self.DoNone(node)
         self.DoExitNone(node)
         return
     if (node.type == "FunctionExpression"):
        self.DoEnterFunctionExpression(node)
        self.DoFunctionExpression(node)
        self.DoExitFunctionExpression(node)
     if (node.type == "AssignmentExpression"):
        self.DoEnterAssignmentExpression(node)
        self.DoAssignmentExpression(node)
        self.DoExitAssignmentExpression(node)
     if (node.type == "MethodDefinition"):
        self.DoEnterMethodDefinition(node)
        self.DoMethodDefinition(node)
        self.DoExitMethodDefinition(node)
     if (node.type == "ExpressionStatement"):
        self.DoEnterExpressionStatement(node)
        self.DoExpressionStatement(node)
        self.DoExitExpressionStatement(node)
     if (node.type == "BinaryExpression"):
        self.DoEnterBinaryExpression(node)
        self.DoBinaryExpression(node)
        self.DoExitBinaryExpression(node)
     if (node.type == "Identifier"):
        self.DoEnterIdentifier(node)
        self.DoIdentifier(node)
        self.DoExitIdentifier(node)
     if (node.type == "Property"):
        self.DoEnterProperty(node)
        self.DoProperty(node)
        self.DoExitProperty(node)
     if (node.type == "ClassDeclaration"):
        self.DoEnterClassDeclaration(node)
        self.DoClassDeclaration(node)
        self.DoExitClassDeclaration(node)
     if (node.type == "BlockStatement"):
        self.DoEnterBlockStatement(node)
        self.DoBlockStatement(node)
        self.DoExitBlockStatement(node)
     if (node.type == "ObjectExpression"):
        self.DoEnterObjectExpression(node)
        self.DoObjectExpression(node)
        self.DoExitObjectExpression(node)
     if (node.type == "AssignmentPattern"):
        self.DoEnterAssignmentPattern(node)
        self.DoAssignmentPattern(node)
        self.DoExitAssignmentPattern(node)
     if (node.type == "ObjectPattern"):
        self.DoEnterObjectPattern(node)
        self.DoObjectPattern(node)
        self.DoExitObjectPattern(node)
     if (node.type == "CallExpression"):
        self.DoEnterCallExpression(node)
        self.DoCallExpression(node)
        self.DoExitCallExpression(node)
     if (node.type == "VariableDeclaration"):
        self.DoEnterVariableDeclaration(node)
        self.DoVariableDeclaration(node)
        self.DoExitVariableDeclaration(node)
     if (node.type == "FunctionDeclaration"):
        self.DoEnterFunctionDeclaration(node)
        self.DoFunctionDeclaration(node)
        self.DoExitFunctionDeclaration(node)
     if (node.type == "VariableDeclarator"):
        self.DoEnterVariableDeclarator(node)
        self.DoVariableDeclarator(node)
        self.DoExitVariableDeclarator(node)
     if (node.type == "ForOfStatement"):
        self.DoEnterForOfStatement(node)
        self.DoForOfStatement(node)
        self.DoExitForOfStatement(node)
     if (node.type == "MemberExpression"):
        self.DoEnterMemberExpression(node)
        self.DoMemberExpression(node)
        self.DoExitMemberExpression(node)
     if (node.type == "TryStatement"):
        self.DoEnterTryStatement(node)
        self.DoTryStatement(node)
        self.DoExitTryStatement(node)
     if (node.type == "ClassBody"):
        self.DoEnterClassBody(node)
        self.DoClassBody(node)
        self.DoExitClassBody(node)
     if (node.type == "CatchClause"):
        self.DoEnterCatchClause(node)
        self.DoCatchClause(node)
        self.DoExitCatchClause(node)
     if (node.type == "Program"):
        self.DoEnterProgram(node)
        self.DoProgram(node)
        self.DoExitProgram(node)
     if (node.type == "IfStatement"):
        self.DoEnterIfStatement(node)
        self.DoIfStatement(node)
        self.DoExitIfStatement(node)

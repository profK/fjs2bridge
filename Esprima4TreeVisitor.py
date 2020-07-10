


class Esprima4TreeVisitor:
    def __init__(self):
        self.indent=""
    def Visit(self,node):
        if(node.type=="Program"):
            self.DoEnterProgram(node)
            self.DoProgram(node)
            self.DoExitProgram(node)
        elif (node.type=="VariableDeclaration"):
            self.DoEnterVariableDeclaration(node)
            self.DoVariableDeclaration(node)
            self.DoExitVariableDeclaration(node)
        elif (node.type=="VariableDeclarator"):
            self.DoEnterVariableDeclarator(node)
            self.DoVariableDeclarator(node)
            self.DoExitVariableDeclarator(node)
        elif (node.type=="Identifier"):
            self.DoEnterIdentifier(node)
            self.DoIdentifier(node)
            self.DoExitIdentifier(node)
        elif (node.type=="ObjectExpression"):
            self.DoEnterObjectExpression(node)
            self.DoObjectExpression(node)
            self.DoExitObjectExpression(node)
        elif (node.type=="ArrayExpression"):
            self.DoEnterArrayExpression(node)
            self.DoArrayExpression(node)
            self.DoExitArrayExpression(node)
        elif (node.type=="id"):
            self.DoEnterID(node)
            self.DoID(node)
            self.DoExitID(node)
        elif (node.type=="Literal"):
            self.DoEnterLiteral(node)
            self.DoLiteral(node)
            self.DoExitLiteral(node)
        elif (node.type=="Property"):
            self.DoEnterProperty(node)
            self.DoProperty(node)
            self.DoExitProperty(node)
        elif (node.type=="ClassDeclaration"):
            self.DoEnterClassDeclaration(node)
            self.DoClassDeclaration(node)
            self.DoExitClassDeclaration(node)
        elif (node.type=="MemberExpression"):
            self.DoEnterMemberExpression(node)
            self.DoMemberExpression(node)
            self.DoExitMemberExpression(node)
        elif (node.type == "UnaryExpression"):
            self.DoEnterUnaryExpression(node)
            self.DoUnaryExpression(node)
            self.DoExitUnaryExpression(node)
        elif (node.type == "CallExpression"):
            self.DoEnterCallExpression(node)
            self.DoCallExpression(node)
            self.DoExitCallExpression(node)
        elif (node.type == "TryStatement"):
            self.DoEnterTryStatement(node)
            self.DoTryStatement(node)
            self.DoExitTryStatement(node)
        elif (node.type == "ExpressionStatement"):
            self.DoEnterExpressionStatement(node)
            self.DoExpressionStatement(node)
            self.DoExitExpressionStatement(node)
        elif (node.type == "FunctionDeclaration"):
            self.DoEnterFunctionDeclaration(node)
            self.DoFunctionDeclaration(node)
            self.DoExitFunctionDeclaration(node)
        elif (node.type == "ClassBody"):
            self.DoEnterClassBody(node)
            self.DoClassBody(node)
            self.DoExitClassBody(node)
        elif (node.type == "NewExpression"):
            self.DoEnterNewExpression(node)
            self.DoNewExpression(node)
            self.DoExitNewExpression(node)
        else:
            print("Unimplemented node type: "+node.type)
    
    def Print(self,string):
        x=2
        #print(self.indent+string)

    def EnterNode(self,name):
        self.Print("Entering "+name)
        self.indent = self.indent+"    "

    def ExitNode(self,name):
        self.indent = self.indent[:len(self.indent)-4]
        self.Print("Exiting "+name)

    def DoEnterProgram(self,node):
        self.EnterNode("Program")

    def DoProgram(self,node):
        for subnode in node.body:
            self.Visit(subnode)

    def DoExitProgram(self,node):
        self.ExitNode("Program")

    def DoEnterVariableDeclaration(self,node):
        self.EnterNode(node.type)

    def DoVariableDeclaration(self,node):
        for subnode in node.declarations:
            self.Visit(subnode)
    def DoExitVariableDeclaration(self,node):
        self.ExitNode(node.type)

    def DoEnterVariableDeclarator(self,node):
        self.EnterNode(node.type)
    def DoVariableDeclarator(self, node):
        self.Visit(node.id)
        self.Visit(node.init)
    def DoExitVariableDeclarator(self,node):
        self.ExitNode(node.type)

    def DoEnterIdentifier(self,node):
        self.EnterNode(node.type)
    def DoIdentifier(self, node):
        self.Print("name: "+node.name)
    def DoExitIdentifier(self,node):
        self.ExitNode(node.type)


    def DoEnterObjectExpression(self,node):
        self.EnterNode(node.type)
    def DoObjectExpression(self,node):
        for property in node.properties:
            self.Visit(property)
    def DoExitObjectExpression(self,node):
        self.ExitNode(node.type)

    def DoEnterArrayExpression(self,node):
        self.EnterNode(node.type)
    def DoArrayExpression(self,node):
        for element in node.elements:
            self.Visit(element)
    def DoExitArrayExpression(self,node):
        self.ExitNode(node.type)

    def DoEnterID(self,node):
        self.EnterNode(node.type)
    def DoID(self,node):
        self.Print("type: "+node.type)
        self.Print("name: "+node.name)
    def DoExitID(self,node):
        self.ExitNode(node.type)

    def DoEnterLiteral(self,node):
        self.EnterNode(node.type)
    def DoLiteral(self,node):
        self.Print("type: "+node.type)
        self.Print("value:"+str(node.value))
    def DoExitLiteral(self,node):
        self.ExitNode(node.type)

    def DoEnterProperty(self,node):
        self.EnterNode(node.type)
    def DoProperty(self,node):
        self.Visit(node.key);
        self.Print("Computed:"+str(node.computed))
        self.Visit(node.value)
        self.Print("kind: "+str(node.kind))
        self.Print("Method: "+str(node.method))
        self.Print("Shorthand: "+str(node.shorthand))
    def DoExitProperty(self,node):
        self.ExitNode(node.type)

    def DoEnterClassDeclaration(self,node):
        self.EnterNode(node.type)
    def DoClassDeclaration(self,node):
        self.Visit(node.id)
        self.Visit(node.body)
    def DoExitClassDeclaration(self,node):
        self.ExitNode(node.type)

    def DoEnterMemberExpression(self,node):
        self.EnterNode(node.type)
    def DoMemberExpression(self,node):
        pass
    def DoExitMemberExpression(self,node):
        self.ExitNode(node.type)

    def DoEnterUnaryExpression(self,node):
        self.EnterNode(node.type)
    def DoUnaryExpression(self,node):
        pass
    def DoExitUnaryExpression(self, node):
        self.ExitNode(node.type)

    def DoEnterCallExpression(self,node):
        self.EnterNode(node.type)
    def DoCallExpression(self,node):
        pass
    def DoExitCallExpression(self, node):
        self.ExitNode(node.type)


    def DoEnterTryStatement(self,node):
        self.EnterNode(node.type)
    def DoTryStatement(self,node):
        pass
    def DoExitTryStatement(self,node):
        self.ExitNode(node.type)

    def DoEnterExpressionStatement(self,node):
        self.EnterNode(node.type)
    def DoExpressionStatement(self,node):
        pass
    def DoExitExpressionStatement(self,node):
        self.ExitNode(node.type)

    def DoEnterFunctionDeclaration(self,node):
        self.EnterNode(node.type)
    def DoFunctionDeclaration(self,node):
        pass
    def DoExitFunctionDeclaration(self,node):
        self.ExitNode(node.type)

    def DoEnterClassBody(self,node):
        self.EnterNode(node.type)
    def DoClassBody(self,node):
        pass
    def DoExitClassBody(self,node):
        self.ExitNode(node.type)

    def DoEnterNewExpression(self,node):
        self.EnterNode(node.type)
    def DoNewExpression(self,node):
        pass
    def DoExitNewExpression(self,node):
        self.ExitNode(node.type)
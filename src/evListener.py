# Generated from ev.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .evParser import evParser
else:
    from evParser import evParser

# This class defines a complete listener for a parse tree produced by evParser.
class evListener(ParseTreeListener):

    # Enter a parse tree produced by evParser#prog.
    def enterProg(self, ctx:evParser.ProgContext):
        pass

    # Exit a parse tree produced by evParser#prog.
    def exitProg(self, ctx:evParser.ProgContext):
        pass


    # Enter a parse tree produced by evParser#line.
    def enterLine(self, ctx:evParser.LineContext):
        pass

    # Exit a parse tree produced by evParser#line.
    def exitLine(self, ctx:evParser.LineContext):
        pass


    # Enter a parse tree produced by evParser#instruction.
    def enterInstruction(self, ctx:evParser.InstructionContext):
        pass

    # Exit a parse tree produced by evParser#instruction.
    def exitInstruction(self, ctx:evParser.InstructionContext):
        pass


    # Enter a parse tree produced by evParser#evCmd.
    def enterEvCmd(self, ctx:evParser.EvCmdContext):
        pass

    # Exit a parse tree produced by evParser#evCmd.
    def exitEvCmd(self, ctx:evParser.EvCmdContext):
        pass


    # Enter a parse tree produced by evParser#lbl.
    def enterLbl(self, ctx:evParser.LblContext):
        pass

    # Exit a parse tree produced by evParser#lbl.
    def exitLbl(self, ctx:evParser.LblContext):
        pass


    # Enter a parse tree produced by evParser#expressionlist.
    def enterExpressionlist(self, ctx:evParser.ExpressionlistContext):
        pass

    # Exit a parse tree produced by evParser#expressionlist.
    def exitExpressionlist(self, ctx:evParser.ExpressionlistContext):
        pass


    # Enter a parse tree produced by evParser#label.
    def enterLabel(self, ctx:evParser.LabelContext):
        pass

    # Exit a parse tree produced by evParser#label.
    def exitLabel(self, ctx:evParser.LabelContext):
        pass


    # Enter a parse tree produced by evParser#argument.
    def enterArgument(self, ctx:evParser.ArgumentContext):
        pass

    # Exit a parse tree produced by evParser#argument.
    def exitArgument(self, ctx:evParser.ArgumentContext):
        pass


    # Enter a parse tree produced by evParser#string_.
    def enterString_(self, ctx:evParser.String_Context):
        pass

    # Exit a parse tree produced by evParser#string_.
    def exitString_(self, ctx:evParser.String_Context):
        pass


    # Enter a parse tree produced by evParser#name.
    def enterName(self, ctx:evParser.NameContext):
        pass

    # Exit a parse tree produced by evParser#name.
    def exitName(self, ctx:evParser.NameContext):
        pass


    # Enter a parse tree produced by evParser#number.
    def enterNumber(self, ctx:evParser.NumberContext):
        pass

    # Exit a parse tree produced by evParser#number.
    def exitNumber(self, ctx:evParser.NumberContext):
        pass


    # Enter a parse tree produced by evParser#work.
    def enterWork(self, ctx:evParser.WorkContext):
        pass

    # Exit a parse tree produced by evParser#work.
    def exitWork(self, ctx:evParser.WorkContext):
        pass


    # Enter a parse tree produced by evParser#flag.
    def enterFlag(self, ctx:evParser.FlagContext):
        pass

    # Exit a parse tree produced by evParser#flag.
    def exitFlag(self, ctx:evParser.FlagContext):
        pass


    # Enter a parse tree produced by evParser#sysFlag.
    def enterSysFlag(self, ctx:evParser.SysFlagContext):
        pass

    # Exit a parse tree produced by evParser#sysFlag.
    def exitSysFlag(self, ctx:evParser.SysFlagContext):
        pass


    # Enter a parse tree produced by evParser#comment.
    def enterComment(self, ctx:evParser.CommentContext):
        pass

    # Exit a parse tree produced by evParser#comment.
    def exitComment(self, ctx:evParser.CommentContext):
        pass



del evParser
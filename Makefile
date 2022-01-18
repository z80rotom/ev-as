.PHONY: clean watch watch-grammar

grammar: grammar/ev_lex.g4 grammar/ev_parse.g4
	antlr -Dlanguage=Python3 grammar/ev_lex.g4 grammar/ev_parse.g4 \
			-o evlang/antlr  -lib grammar -Xexact-output-dir

watch-grammar: 
	make watch WATCHMAKE=grammar

watch: 
	while true; do \
		make $(WATCHMAKE); \
		fswatch -1 grammar/ev_lex.g4 grammar/ev_parse.g4; \
	done


clean: 
	rm -rf build

married(chagai,ronit).
married(baruchi,chavi).
married(udi, michal).
parent(ronit,chavi).
parent(ronit,zili). 
parent(chagai,tehila).
parent(chagai,zili).
parent(chagai,hadasa).
parent(chagai,chavi).
parent(chagai,rehut).
parent(ronit,hadasa).
parent(ronit,tehila).
parent(ronit,rehut).
parent(neomi,chagai).
parent(neomi,michal).
parent(michal,tami).
parent(michal,yosi).
parent(nachum, chagai).
parent(chavi, noa).
parent(tami, lea).
male(chagai).
male(baruchi).
male(yosi).
female(ronit).
female(chavi).
female(zili).
female(tami).
female(hadasa).
female(tehila).
female(michal).


father(X, Y):-parent(X,Y), male(X).
mother(X,Y):-parent(X,Y), female(X).
son(X,Y):-parent(Y,X),male(X).
daughter(X,Y):-parent(Y,X),female(X).
grandfather(X,Y):-parent(X,Z),parent(Z,Y),male(X).
grandmother(X,Y):-parent(X,Z),parent(Z,Y),female(X).
grandson(X,Y):-parent(Z,X),parent(Y,Z),male(X).
granddaughter(X,Y):-parent(Z,X),parent(Y,Z),female(X).
sibling(X,Y):-parent(Z,X),parent(Z,Y), X \= Y.
uncle(X,Y):-sibling(X,Z),parent(Z,Y),male(X).
boycousin(X,Y):-parent(W,X),parent(Z,Y),sibling(W,Z),male(X).
cousin(X,Y):-parent(W,X),parent(Z,Y),sibling(W,Z).
brotherinlaw(X,Y):-married(X,Z),sibling(Y,Z).
niece(X,Y):-daughter(X,Z),sibling(Y,Z).
cousins2(X,Y):-parent(Z,X),parent(W,Y),cousin(Z,W).

reverse([],[]).
reverse([H|T],R):-
    reverse(T,R1),append(R1,[H],R).
    
member(X, [X|_]).
member(X,[_ | T]):-
    member(X,T).



palindrom([]).
palindrom([_]).
palindrom([H|T]):-
    append(R,[H],T),
    palindrom(R).

sorted([]).
sorted([_]).
sorted([X, Y | T]) :- X =< Y, sorted([Y | T]).


permutation([], []).
permutation(L, [H|T]) :- select(H, L, R), permutation(R, T).



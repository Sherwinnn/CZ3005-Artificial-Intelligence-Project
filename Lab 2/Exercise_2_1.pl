% State the fact
queen(elizabeth).

offspring(charles,elizabeth).
offspring(andrew,elizabeth).
offspring(edward,elizabeth).
offspring(ann,elizabeth).

male(charles).
male(andrew).
male(edward).
female(ann).

older(charles, ann).
older(ann, andrew).
older(andrew, edward).

% Transitive Rule
% If X is older than Y and Y is older than Z, then X is older than Z
isOlder(X,Y) :- older(X,Y).
isOlder(X,Z) :- older(X,Y),isOlder(Y,Z).

% Help in comparator
sameGender(X,Y) :- ( male(X),male(Y));(female(X),female(Y)).

% comparator define the rules in comparing the order
% X is before Y if
% Rule 1: X is male, Y is female
% Rule 2: If X and Y is same gender, X is older than Y
comparator(X,Y) :- ( male(X),female(Y)) ; (sameGender(X,Y), isOlder(X,Y)).

% Insertion Sort
insertSort(List,Result):- recursiveSort(List,[],Result).
recursiveSort([],Acc,Acc).
recursiveSort([H|T],Acc,Result):- insert(H,Acc,NewAcc),recursiveSort(T,NewAcc,Result).

insert(X,[Y|T],[X,Y|T]):-comparator(X,Y).
insert(X,[Y|T],[Y|NT]):-not(comparator(X,Y)),insert(X,T,NT).
insert(X,[],[X]).

% Provide the queen name and will return the successions in Results
royalSuccession(Queen, Results):- queen(Queen), findall(X, offspring(X, Queen), Candidates),  insertSort(Candidates, Results).








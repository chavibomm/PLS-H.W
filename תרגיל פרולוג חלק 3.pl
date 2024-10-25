sum(N,RES):-
    N>1,
    sum(N,RES,0).
sum(0,RES,RES).
sum(N,RES,ACC):-
    N1 is N-1,
    ACC1 is ACC+N,
    sum(N1,RES,ACC1).


sumDigits(Num, Sum) :-
    sumDigits(Num, Sum, 0).

sumDigits(0, Sum, Sum).
sumDigits(Num, Sum, Acc) :-
    Num > 0,
    Digit is Num mod 10,
    Num1 is Num // 10,
    Acc1 is Acc + Digit,
    sumDigits(Num1, Sum, Acc1).



split(Num, L):-
    split(Num,L,[]).

split(0,L,L).
split(Num,L,Acc):-
    Digit is Num mod 10,
    Num1 is Num // 10,
    split(Num1,L,[Digit|Acc]).


create(List, N) :- 
    reverse(List, Reversed),   % להפוך את הרשימה כדי שהספרות יהיו בסדר הנכון
    create_number(Reversed, 0, N).  % להתחיל עם ערך 0

create_number([], N, N).  % כשאין עוד ספרות, N הוא התוצאה
create_number([Digit|Rest], Acc, N) :- 
    NewAcc is Acc * 10 + Digit,  % להכפיל את הערך הנוכחי בעשר ולהוסיף את הספרה הנוכחית
    create_number(Rest, NewAcc, N).  % להמשיך עם שאר הספרות


reversedNumber(N,R):-
    split(N,L), create(L,R).
    
intersection([], _, []).  % אם הרשימה הראשונה ריקה, החיתוך הוא ריק
intersection([H|T], L2, [H|Z]) :- 
    member(H, L2),         % אם האיבר H נמצא ברשימה השנייה
    intersection(T, L2, Z). % המשך לחתוך את שאר הרשימה
intersection([H|T], L2, Z) :- 
    \+ member(H, L2),      % אם האיבר H לא נמצא ברשימה השנייה
    intersection(T, L2, Z). % המשך לחתוך את שאר הרשימה
    

minus([], _, []).  % אם הרשימה הראשונה ריקה, החיסור הוא ריק
minus([H|T], L2, [H|Z]) :- 
    \+ member(H, L2),     % אם האיבר H לא נמצא ברשימה השנייה
    minus(T, L2, Z).      % המשך לחסור את שאר הרשימה
minus([H|T], L2, Z) :- 
    member(H, L2),        % אם האיבר H נמצא ברשימה השנייה
    minus(T, L2, Z).      % המשך לחסור את שאר הרשימה




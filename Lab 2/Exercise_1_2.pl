% State facts
company(sumsum).
company(appy).

smart_phone_technology(galacticas3).

competitor(appy,sumsum).

steal(stevey,galacticas3).
develop(sumsum,galacticas3).


% Stevey is a boss to appy
boss(stevey,appy).


% A smart phone technology is a business
business(X):- smart_phone_technology(X).

% Rival 
%rival(Company1,Company2):- competitor(Company1,Company2);competitor(Company2,Company1).
rival(appy,Company2):- competitor(appy,Company2).
% Unethical
unethical(Person):- 
    boss(Person,Company1),
    company(Company1),
    rival(Company1,Company2),
    company(Company2),
    business(Product),
    steal(Person,Product),
    develop(Company2,Product).

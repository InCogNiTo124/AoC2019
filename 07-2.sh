for permutation in $(./permute 01234); do
    #echo $permutation;
    input=0;
    pipexec -- \
        #[ Z /usr/bin/echo $input ] \
        [ A /usr/bin/python3 07-2.py < <(/usr/bin/python3 phase ${permutation:0:1}) ] \
        [ B /usr/bin/python3 07-2.py < <(/usr/bin/python3 phase ${permutation:1:1}) ] \
        [ C /usr/bin/python3 07-2.py < <(/usr/bin/python3 phase ${permutation:2:1}) ] \
        [ D /usr/bin/python3 07-2.py < <(/usr/bin/python3 phase ${permutation:3:1}) ] \
        [ E /usr/bin/python3 07-2.py < <(/usr/bin/python3 phase ${permutation:4:1}) ] \
        #"{Z:1>A:0}" \
        "{A:1>B:0}" \
        "{B:1>C:0}" \
        "{C:1>D:0}" \
        "{D:1>E:0}" \
        "{E:1>A:0}"
done

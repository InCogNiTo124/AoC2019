for permutation in $(./permute 01234); do
    input=0;
    for char in $(echo $permutation | sed 's/./& /g'); do
        input=$(echo -e "${char}\n${input}" | python3 07.py)
    done
    echo $input;
done

num_writer() {
    echo $1 >> "rands_${num_rands}.txt"
}
if [ -z "$1" ]; then
    echo "Usage: $0 num_rands [min] [max]"
    exit 1
fi
num_rands=$1
min=${2:-1}
max=${3:-32767}
sum=0
smallest=$max
largest=$min
> "rands_${num_rands}.txt"
for ((i=0; i<num_rands; i++)); do
    rand_num=$((RANDOM % (max - min + 1) + min))
    num_writer $rand_num
    sum=$((sum + rand_num))
    if [ $rand_num -lt $smallest ]; then
        smallest=$rand_num
    fi
    if [ $rand_num -gt $largest ]; then
        largest=$rand_num
    fi
done

average=$(echo "scale=2; $sum / $num_rands" | bc)

echo "You requested $num_rands numbers [between $min and $max]"
echo "The smallest value generated was $smallest"
echo "The largest value generated was $largest"
echo "Average: $average"
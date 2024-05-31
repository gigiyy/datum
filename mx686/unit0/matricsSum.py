def get_sum_metrics(predictions, metrics=[]):
    current = metrics.copy()
    for i in range(3):
        current.append(eval("lambda x: x + " + str(i)))

    sum_metrics = 0
    for metric in current:
        sum_metrics += metric(predictions)

    return sum_metrics


x = 6
y = get_sum_metrics(6)
print(y)
z = get_sum_metrics(5)
print(z)




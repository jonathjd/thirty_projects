def parse_fastq(input_fastq):
    with open(input_fastq, "r") as input_handle:
        for line in input_handle:
            next(input_handle)
            next(input_handle)
            yield next(input_handle).rstrip()


def calculate_phred_scores(quality_score):
    return [ord(char) - 33 for char in quality_score]


def main():
    sum_scores = []
    record_count = 0

    for quality_scores in parse_fastq("data/fastq_files/demo.fastq"):
        phred_scores = calculate_phred_scores(quality_scores)

        if len(phred_scores) > len(sum_scores):
            sum_scores += [0] * (len(phred_scores) - len(sum_scores))

        for pos, score in enumerate(phred_scores):
            if pos < len(sum_scores):
                sum_scores[pos] += score

        record_count += 1

    if record_count > 0:
        average_scores = [sum_score / record_count for sum_score in sum_scores]
        for pos, avg_score in enumerate(average_scores):
            print(f"Position {pos+1}: Average Score = {avg_score:.2f}")

    else:
        print("No record found")


if __name__ == "__main__":
    main()

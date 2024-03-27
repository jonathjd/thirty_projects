import sys
import csv
import gzip


def parse_fastq(input_fastq):
    if input_fastq.endswith(".gz"):  # Use gzip.open for gzipped files
        with gzip.open(input_fastq, "rt") as input_handle:
            for line in input_handle:
                next(input_handle)
                next(input_handle)
                yield next(input_handle).rstrip()
    else:
        with open(input_fastq, "r") as input_handle:
            for line in input_handle:
                next(input_handle)
                next(input_handle)
                yield next(input_handle).rstrip()


def calculate_phred_scores(quality_score):
    return [ord(char) - 33 for char in quality_score]


def write_base_qualities_to_csv(average_quality, csv_output):

    with open(csv_output, mode="w") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(["Base Position", "Average Quality Score"])
        for i, score in enumerate(average_quality, start=1):
            writer.writerow([i, score])
    return


def main(fastq_file, csv_output):
    sum_scores = []
    record_count = 0

    for quality_scores in parse_fastq(fastq_file):
        phred_scores = calculate_phred_scores(quality_scores)

        if len(phred_scores) > len(sum_scores):
            sum_scores += [0] * (len(phred_scores) - len(sum_scores))

        for pos, score in enumerate(phred_scores):
            if pos < len(sum_scores):
                sum_scores[pos] += score

        record_count += 1

    if record_count > 0:
        average_scores = [sum_score / record_count for sum_score in sum_scores]

        write_base_qualities_to_csv(
            average_quality=average_scores, csv_output=csv_output
        )

    else:
        print("No record found")


if __name__ == "__main__":
    fastq_file, csv_output = sys.argv[1], sys.argv[2]
    main(fastq_file=fastq_file, csv_output=csv_output)

version 1.0

task CalculateBaseQuality {
    input {
        File fastq_input
        String csv_output
    }

    command {
        python /app/parse_fastq.py ~{fastq_input} ~{csv_output}
    }

    runtime {
        docker: "jonathjd/mywdl_image1:v1"
    }

    output {
        File output_csv = csv_output
    }
}

workflow CalculateBaseQualityWorkflow {
    input {
        File input_fastq
        String output_name = "base_quality.csv"
    }

    call CalculateBaseQuality {
        input:
            fastq_input = input_fastq,
            csv_output = output_name
    }

    output {
        File base_quality_csv = CalculateBaseQuality.output_csv
    }
}
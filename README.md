# RC - Snippets for Recurse Application

## CracklePop in RISC-V

I wanted to do something acoustic, or as some might say, even analog. This is an implementation of Fizzbuzz aka CracklePop for the Recurse Center application. This implementation is RISC-V, and I'm proud to say that it's written by hand and brain. LLMs were used to fix any errors, but the main logic and 95% of it is logic and code that I have thought through by looking at documentation. LLMs were solely used for handling any reasons as to why there's errors, and documentation was used to fix the proposed-solution to the errors.

### Instructions to Run:

```
download RARS - https://github.com/TheThirdOne/rars/releases
java -jar ~/Downloads/rars1_6.jar nc me cracklepop.s > result.txt
```

### What is the Recurse Center? Why write this?
One of the easiest way to describe the Recurse Center is 'a writer's retreat for programmers'. I appreciate constant education and enjoy discussing technical topics with others. As I've been curious about Recurse Center for almost a decade, I'm excited to complete this application. 

### Shoutouts and Resources
Huge thank you to the following resources:
University of Alberta's Computer Organization and Architecture labs and documentation. Impressively great documentation, and encouraging to see thoroughly educational open-source resources still exist. 

RARS, a RISC-V Assembler and Runtime Simulator: [RARS](https://github.com/TheThirdOne/rars/releases)
Great online  RISC-V Assembler here: [Online RISC-V Assembler](https://riscvasm.lucasteske.dev/)

For an official citation of this great online assembler:
```
@misc{teske2026riscvasm,
  title={RISC-V Online Assembler},
  author={Teske, Lucas},
  year={2026},
  publisher={Zenodo},
  version={1.0.0},
  doi={10.5281/zenodo.21526003},
  url={https://doi.org/10.5281/zenodo.21526003},
  note={Browser-based RISC-V assembler powered by a WebAssembly build of GNU binutils. Live tool: https://riscvasm.lucasteske.dev/. Source: https://github.com/racerxdl/riscv-online-asm. ORCID: 0009-0002-8526-7662}
}
```

Really helpful reference for syscall conventions in RISC-V: [RISC-V documentation](https://asm-editor.specy.app/documentation/risc-v/syscall) 

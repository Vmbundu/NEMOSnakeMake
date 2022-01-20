rule ccd3:
     output: 'ccd.in'
     shell:  'ccdmath out={output} "fie=10*%x+sqrt(%y)"  size=10,10,1'

rule ccdprint:
     input: 'ccd.in'
     log: 'output.log'
     shell: 'ccdprint {input} x= y= format=%7.3f; nemo.coverage ccdprint.c > {log}'

rule ccdhead:
     input: 'ccd.in'
     shell: 'ccdhead {input}'



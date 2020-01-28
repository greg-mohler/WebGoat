pipeline {
   agent any
   stages {
      stage('Security Check') {
         steps {
             //check if code passes security tests:
             script {
                 int threshold = 50
                 Random rnd = new Random()
                 int num = rnd.nextInt(99)
                 println('Security score: ' + num + ' / 100')
                 if(num < threshold){
                     println('Your security score was too low to qualify for a reward.')
                     error("Build failed because of a low security score.")
                 }
                 else{
                     println('Your security score qualifies you for a chance at a reward!')
                 }
             }
         }
      }
      stage('Generate Chance') {
         steps {
             script{
                 int threshold = 50
                 int reward = 25
                 Random rnd = new Random()
                 int num = rnd.nextInt(99)
                 println('Reward Roll: ' + num + ' / 100')
                 if(num < threshold){
                     println('You did not receive a reward.')
                     error("Build failed because of a missed reward roll.")
                 }
                 else{
                     println('Congratulations! You just receieved a reward of $' + reward +'!')
                 }
             }
         }
      }
   }
}

//
//
import './Component.css';
const AboutPage = (props) => {

  return(
    <div className='about-page hide-small'>
      <div className='app-stack' >
        <h2>Application Stack</h2>
        <a href='https://github.com/FullStackWithLawrence/aws-openai' target="_blank">
          <img src='/app-stack.jpeg' />
        </a>
      </div>
    </div>

  )
}

export default AboutPage;

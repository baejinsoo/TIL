import React from 'react';
import PropTypes from 'prop-types';

// const MyComponent = props => {
//     const { name, children } = props;
//     return (
//         <div>
//             나의 새롭고 멋진 컴포넌트 {name}입니다.<br />
//             children 값은 {children}
//         </div>
//     );
// };
const MyComponent = ({ name, children, favoriteNumber }) => {
    return (
        <div>
            나의 새롭고 멋진 컴포넌트 {name}입니다.<br />
            children 값은 {children} 입니다 <br />
            제가 좋아하는 숫자는 {favoriteNumber}입니다. <br />
        </div>
    );
};

MyComponent.defaultProps = {
    name: '기본 이름'
};

MyComponent.propTypes = {
    name: PropTypes.string, // name 값은 무조건 문자열 형태로 전달해야 된다는 것을 의미
    favoriteNumber: PropTypes.number.isRequired // propTypes를 지정하지 않으면 안됨
};

export default MyComponent;
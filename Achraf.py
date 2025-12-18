import random
import string
import secrets
import argparse
from typing import List, Optional

class PasswordGenerator:
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = string.punctuation
        
    def generate_password(self, 
                         length: int = 12,
                         use_uppercase: bool = True,
                         use_digits: bool = True,
                         use_symbols: bool = True,
                         exclude_similar: bool = False) -> str:
        """
        توليد كلمة مرور واحدة مع خيارات التخصيص
        """
        # إنشاء مجموعة الأحرف المسموحة
        chars = self.lowercase
        
        if use_uppercase:
            chars += self.uppercase
        if use_digits:
            chars += self.digits
        if use_symbols:
            chars += self.symbols
            
        # استبعاد الأحرف المتشابهة إذا طلب
        if exclude_similar:
            similar_chars = 'il1Lo0O'
            chars = ''.join([c for c in chars if c not in similar_chars])
            
        # التأكد من وجود طول كافي
        if len(chars) == 0:
            raise ValueError("لم يتم اختيار أي نوع من الأحرف!")
            
        if length < 4:
            raise ValueError("الطول يجب أن يكون 4 أحرف على الأقل")
            
        # توليد كلمة مرور قوية باستخدام secrets
        password = ''.join(secrets.choice(chars) for _ in range(length))
        
        # التحقق من توفر جميع أنواع الأحرف المطلوبة
        if use_uppercase and not any(c.isupper() for c in password):
            password = self._ensure_character_type(password, self.uppercase, chars)
        if use_digits and not any(c.isdigit() for c in password):
            password = self._ensure_character_type(password, self.digits, chars)
        if use_symbols and not any(c in self.symbols for c in password):
            password = self._ensure_character_type(password, self.symbols, chars)
            
        return password
    
    def _ensure_character_type(self, password: str, char_type: str, all_chars: str) -> str:
        """
        التأكد من وجود نوع محدد من الأحرف في كلمة المرور
        """
        password_list = list(password)
        # استبدال حرف عشوائي بنوع الحرف المطلوب
        index = secrets.randbelow(len(password))
        password_list[index] = secrets.choice(char_type)
        return ''.join(password_list)
    
    def generate_passwords_list(self, 
                               count: int = 10,
                               length: int = 12,
                               use_uppercase: bool = True,
                               use_digits: bool = True,
                               use_symbols: bool = True,
                               exclude_similar: bool = False) -> List[str]:
        """
        توليد قائمة من كلمات المرور
        """
        passwords = []
        for i in range(count):
            try:
                pwd = self.generate_password(
                    length=length,
                    use_uppercase=use_uppercase,
                    use_digits=use_digits,
                    use_symbols=use_symbols,
                    exclude_similar=exclude_similar
                )
                passwords.append(pwd)
            except ValueError as e:
                print(f"خطأ في توليد كلمة المرور {i+1}: {e}")
                continue
                
        return passwords
    
    def calculate_strength(self, password: str) -> str:
        """
        تقييم قوة كلمة المرور
        """
        length = len(password)
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_symbol = any(c in self.symbols for c in password)
        
        score = 0
        if length >= 12:
            score += 2
        elif length >= 8:
            score += 1
            
        score += has_upper + has_lower + has_digit + has_symbol
        
        if score >= 6:
            return "قوي جدًا"
        elif score >= 4:
            return "قوي"
        elif score >= 2:
            return "متوسط"
        else:
            return "ضعيف"
    
    def save_to_file(self, passwords: List[str], filename: str = "passwords.txt"):
        """
        حفظ كلمات المرور في ملف
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("قائمة كلمات المرور المولدة:\n")
                f.write("=" * 30 + "\n")
                for i, pwd in enumerate(passwords, 1):
                    strength = self.calculate_strength(pwd)
                    f.write(f"{i:3}. {pwd} - [{strength}]\n")
            print(f"تم حفظ {len(passwords)} كلمة مرور في ملف {filename}")
        except Exception as e:
            print(f"خطأ في حفظ الملف: {e}")

def main():
    parser = argparse.ArgumentParser(
        description='أداة توليد قوائم كلمات مرور مخصصة',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
أمثلة:
  %(prog)s -c 5 -l 16
  %(prog)s -c 10 -l 12 --no-symbols
  %(prog)s -c 8 -l 14 --exclude-similar
        """
    )
    
    parser.add_argument('-c', '--count', type=int, default=10,
                       help='عدد كلمات المرور المراد توليدها (افتراضي: 10)')
    parser.add_argument('-l', '--length', type=int, default=12,
                       help='طول كل كلمة مرور (افتراضي: 12)')
    parser.add_argument('--no-uppercase', action='store_false', dest='uppercase',
                       help='عدم استخدام الأحرف الكبيرة')
    parser.add_argument('--no-digits', action='store_false', dest='digits',
                       help='عدم استخدام الأرقام')
    parser.add_argument('--no-symbols', action='store_false', dest='symbols',
                       help='عدم استخدام الرموز الخاصة')
    parser.add_argument('-e', '--exclude-similar', action='store_true',
                       help='استبعاد الأحرف المتشابهة (مثل: il1Lo0O)')
    parser.add_argument('-o', '--output', type=str,
                       help='اسم ملف الحفظ (افتراضي: passwords.txt)')
    parser.add_argument('-s', '--show-strength', action='store_true',
                       help='عرض قوة كل كلمة مرور')
    
    args = parser.parse_args()
    
    # إنشاء مولد كلمات المرور
    generator = PasswordGenerator()
    
    print("\n" + "="*50)
    print("     أداة توليد قوائم كلمات المرور")
    print("="*50)
    
    print(f"\nالإعدادات:")
    print(f"  عدد كلمات المرور: {args.count}")
    print(f"  طول كل كلمة مرور: {args.length}")
    print(f"  الأحرف الكبيرة: {'نعم' if args.uppercase else 'لا'}")
    print(f"  الأرقام: {'نعم' if args.digits else 'لا'}")
    print(f"  الرموز الخاصة: {'نعم' if args.symbols else 'لا'}")
    print(f"  استبعاد المتشابهة: {'نعم' if args.exclude_similar else 'لا'}")
    
    # توليد كلمات المرور
    try:
        passwords = generator.generate_passwords_list(
            count=args.count,
            length=args.length,
            use_uppercase=args.uppercase,
            use_digits=args.digits,
            use_symbols=args.symbols,
            exclude_similar=args.exclude_similar
        )
        
        print(f"\n{'='*50}")
        print("     كلمات المرور المولدة:")
        print('='*50)
        
        for i, pwd in enumerate(passwords, 1):
            strength_info = ""
            if args.show_strength:
                strength = generator.calculate_strength(pwd)
                strength_info = f" - [{strength}]"
            print(f"{i:3}. {pwd}{strength_info}")
        
        # حفظ في ملف إذا طلب
        if args.output:
            generator.save_to_file(passwords, args.output)
        elif len(passwords) > 0:
            save = input("\nهل تريد حفظ كلمات المرور في ملف؟ (نعم/لا): ")
            if save.lower() in ['نعم', 'yes', 'y']:
                filename = input("اسم الملف (افتراضي: passwords.txt): ").strip()
                filename = filename if filename else "passwords.txt"
                generator.save_to_file(passwords, filename)
        
        print("\n" + "="*50)
        print("تمت العملية بنجاح!")
        print("="*50)
        
    except ValueError as e:
        print(f"\nخطأ: {e}")
    except Exception as e:
        print(f"\nحدث خطأ غير متوقع: {e}")

if __name__ == "__main__":
    main()
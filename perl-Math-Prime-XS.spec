#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Math-Prime-XS
Version  : 0.27
Release  : 15
URL      : https://cpan.metacpan.org/authors/id/K/KR/KRYDE/Math-Prime-XS-0.27.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KR/KRYDE/Math-Prime-XS-0.27.tar.gz
Summary  : 'Detect and calculate prime numbers with deterministic tests'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Math-Prime-XS-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Params::Validate)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(boolean)

%description
NAME
Math::Prime::XS - Detect and calculate prime numbers with deterministic
tests

%package dev
Summary: dev components for the perl-Math-Prime-XS package.
Group: Development
Provides: perl-Math-Prime-XS-devel = %{version}-%{release}
Requires: perl-Math-Prime-XS = %{version}-%{release}

%description dev
dev components for the perl-Math-Prime-XS package.


%package perl
Summary: perl components for the perl-Math-Prime-XS package.
Group: Default
Requires: perl-Math-Prime-XS = %{version}-%{release}

%description perl
perl components for the perl-Math-Prime-XS package.


%prep
%setup -q -n Math-Prime-XS-0.27
cd %{_builddir}/Math-Prime-XS-0.27

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Math::Prime::XS.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/Math/Prime/XS.pm
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Math/Prime/XS/XS.so
